from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import JobViewSet, CompanyViewSet

router = DefaultRouter()
router.register(r'jobs', JobViewSet)
router.register(r'companies', CompanyViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
