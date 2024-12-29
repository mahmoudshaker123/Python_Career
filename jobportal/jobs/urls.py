from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.routers import DefaultRouter
from . import views

urlpatterns = [
    path('', views.index, name='index'),
     path('jobs/', views.job_list, name='job_list'),
    path('search/', views.job_search, name='job_search'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router = DefaultRouter()