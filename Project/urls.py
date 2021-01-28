from django.contrib import admin


from django.urls import path, include
from rest_framework import routers

from data_source import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'employee', views.EmployeeViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    path('data_source/', include('data_source.urls'))
]

