from django.conf.urls import url, include
from rest_framework import routers
from profiles import views

# router = routers.DefaultRouter()
# router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     url(r'^', include(router.urls)),
#     # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]

urlpatterns = [
    url(r'^$', views.UserListView.as_view()),
    url(r'^(?P<username>[A-Za-z0-9]+)/$', views.UserDetailView.as_view()),
]
