from django.shortcuts import render
from rest_framework import viewsets
from .models import Job, Company
from .serializers import JobSerializer, CompanySerializer

class JobViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
