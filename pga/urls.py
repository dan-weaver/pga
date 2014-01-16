from api import views
from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from django.contrib import admin

router = DefaultRouter()
router.register(r'golfers', views.GolferViewSet)
router.register(r'events', views.EventViewSet)
router.register(r'results', views.ResultViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pga.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls)),
)
