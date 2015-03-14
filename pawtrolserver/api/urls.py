from django.conf.urls import patterns, include, url

from api.views import LogoutView


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pawtrolserver.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^login/', 'rest_framework.authtoken.views.obtain_auth_token'),
    url(r'^logout/', LogoutView.as_view()),
    
)
