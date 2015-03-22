from django.conf.urls import patterns, include, url
from django.contrib import admin

from rest_framework.urlpatterns import format_suffix_patterns

# from api import urls as api_urls
from profiles import urls as profiles_urls


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pawtrolserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    # url(r'^', include(api_urls)),
    url(r'^profiles/', include(profiles_urls)),
)

urlpatterns = format_suffix_patterns(urlpatterns)
