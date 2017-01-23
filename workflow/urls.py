from django.conf.urls import url

from . import views

app_name = 'workflow'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^project/(?P<project_id>[0-9]+)/issue/(?P<issue_id>[0-9]+)/$',
        views.issue, name='issue'),
    url(r'^project/(?P<project_id>[0-9]+)/sprint/(?P<sprint_id>[0-9]+)/$',
        views.SprintView.as_view(), name='sprint'),
]
