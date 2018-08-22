from django.apps import AppConfig
from django.db.models import signals


class MarketplacePackageConfig(AppConfig):
    name = 'waldur_mastermind.marketplace_packages'
    verbose_name = 'Marketplace VPC packages'

    def ready(self):
        from waldur_core.structure import models as structure_models
        from waldur_mastermind.packages import models as package_models
        from waldur_mastermind.marketplace.plugins import manager

        from . import handlers, processor

        signals.post_save.connect(
            handlers.create_offering_and_plan_for_package_template,
            sender=package_models.PackageTemplate,
            dispatch_uid='waldur_mastermind.marketpace_packages.'
                         'create_offering_and_plan_for_package_template',
        )

        signals.post_save.connect(
            handlers.update_offering_for_service_settings,
            sender=structure_models.ServiceSettings,
            dispatch_uid='waldur_mastermind.marketpace_packages.'
                         'update_offering_for_service_settings',
        )

        manager.register('Packages.Template', processor.process_order_item)