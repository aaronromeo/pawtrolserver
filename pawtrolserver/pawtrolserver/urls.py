from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

# from api import urls as api_urls
from profiles import urls as profiles_urls
from profiles.views import (
    CurrentUserView,
    OwnerListView,
    ServiceBusinessDetailView,
    ServiceBusinessListView,
    ServiceBusinessWalkerListView,
    WalkerListView,
)


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pawtrolserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^', include(api_urls)),
    url(r'^profiles/', include(profiles_urls)),

    url(r'^profile/', CurrentUserView.as_view()),
    url(r'^owners/', OwnerListView.as_view()),
    url(r'^walkers/', WalkerListView.as_view()),

    url(r'^business/$', ServiceBusinessListView.as_view()),
    url(r'^business/(?P<uuid>[A-Za-z0-9]+)/$', ServiceBusinessDetailView.as_view()),
    url(r'^business/(?P<business_uuid>[A-Za-z0-9]+)/walkers/$', ServiceBusinessWalkerListView.as_view()),

)

urlpatterns = format_suffix_patterns(urlpatterns)
