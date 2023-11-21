# myapi/urls.py
from django.urls import include, path
from rest_framework import routers
from . import views
from . import controllers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'records', views.RecordViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', views.UserView.as_view(), name='user'),
    path('ifc/', views.IfcView.as_view(), name = 'ifc'),
]