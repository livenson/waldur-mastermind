from __future__ import unicode_literals

from django.conf.urls import patterns
from django.conf.urls import url

from nodeconductor_assembly_waldur.support import views


def register_in(router):
    router.register(r'support-issues', views.IssueViewSet, base_name='support-issue')
    router.register(r'support-comments', views.CommentViewSet, base_name='support-comment')
    router.register(r'support-users', views.SupportUserViewSet, base_name='support-user')

urlpatterns = patterns(
    '',
    url(r'^api/support-jira-webhook/$', views.WebHookReceiverView.as_view(), name='web-hook-receiver'),
    url(r'^api/offering/$', views.OfferingListView.as_view(), name='offering-list'),
    url(r'^api/offering/(?P<name>\w+)/$', views.OfferingView.as_view(), name='offering-detail'),
)
