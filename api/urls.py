from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

from api import views

urlpatterns = patterns('api.views',
	url(r'^api/golfers/$', views.GolferList.as_view()),
	url(r'^api/golfers/(?P<pk>[0-9]+)/$', views.GolferDetail.as_view()),
	url(r'^api/results/$', views.ResultsList.as_view()),
	url(r'^api/results/(?P<pk>[0-9]+)/$', views.ResultsDetail.as_view()),
	url(r'^api/events/(?P<pk>[0-9]+)/$', views.EventsDetail.as_view()),
	url(r'^api/events/$', views.EventsList.as_view())

)

uelpatterns = format_suffix_patterns(urlpatterns)