import mock

from waldur_core.core import tasks as core_tasks

from waldur_mastermind.packages import executors


def run_openstack_package_change_executor(package, new_template):
    with mock.patch.object(core_tasks.BackendMethodTask, 'get_backend'):
        executors.OpenStackPackageChangeExecutor.execute(package.tenant,
                                                         new_template=new_template,
                                                         old_package=package,
                                                         service_settings=package.service_settings,
                                                         async=False)
