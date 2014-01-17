from django.conf.urls import patterns, include, url
from django.contrib import admin
import api


urlpatterns = patterns('',
    # Examples:
    url(r'^', include('api.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
