from django.core.exceptions import ObjectDoesNotExist
from rest_framework import serializers, status
from rest_framework.reverse import reverse

from waldur_core.structure import models as structure_models
from waldur_mastermind.common.utils import internal_api_request
from waldur_slurm import models as slurm_models
from waldur_slurm import views as slurm_views
from waldur_slurm.apps import SlurmConfig


def process_slurm(order_item, user):
    try:
        service_settings = order_item.offering.scope
    except ObjectDoesNotExist:
        service_settings = None

    if not isinstance(service_settings, structure_models.ServiceSettings):
        raise serializers.ValidationError('Offering has invalid scope. Service settings is expected.')

    if service_settings.type != SlurmConfig.service_name:
        raise serializers.ValidationError('Offering has invalid scope type.')

    project = order_item.order.project

    try:
        spl = slurm_models.SlurmServiceProjectLink.objects.get(
            project=project,
            service__settings=service_settings,
            service__customer=project.customer,
        )
    except slurm_models.SlurmServiceProjectLink.DoesNotExist:
        raise serializers.ValidationError('Project does not have access to the SLURM service.')

    fields = (
        'cpu_limit',
        'gpu_limit',
        'ram_limit',
    )
    spl_url = reverse('slurm-spl-detail', kwargs={'pk': spl.pk})
    payload = dict(
        name=order_item.offering.name,
        service_project_link=spl_url,
    )

    for field in fields:
        if field in order_item.attributes:
            payload[field] = order_item.attributes.get(field)

    view = slurm_views.AllocationViewSet.as_view({'post': 'create'})
    response = internal_api_request(view, user, payload)
    if response.status_code != status.HTTP_201_CREATED:
        raise serializers.ValidationError(response.data)

    allocation_uuid = response.data['uuid']
    allocation = slurm_models.Allocation.objects.get(uuid=allocation_uuid)
    order_item.scope = allocation
    order_item.save()
