from nodeconductor.core import tasks as core_tasks
from nodeconductor_openstack import models as openstack_models


class OpenStackPackageErrorTask(core_tasks.ErrorStateTransitionTask):
    """ Handle OpenStack package creation errors.

        If error occurred on tenant creation - mark tenant and service settings as erred.
        If error occurred on service settings creation - mark only service settings as erred.
    """

    @classmethod
    def get_description(cls, result_id, package, *args, **kwargs):
        return 'Mark package "%s" components as erred.' % package

    def execute(self, package):
        if package.tenant.state != openstack_models.Tenant.States.OK:
            self.state_transition(package.tenant, 'set_erred')
            self.save_error_message(package.tenant)
            self.state_transition(package.service_settings, 'set_erred')
            package.service_settings.error_message = 'Failed to create tenant: %s.' % package.tenant
            package.service_settings.save(update_fields=['error_message'])
        else:
            self.state_transition(package.service_settings, 'set_erred')
            self.save_error_message(package.service_settings)
