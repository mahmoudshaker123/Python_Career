from django.shortcuts import render
from .models import *

def index(request):
    jobs = Job.objects.all()
    return render(request, 'index.html', {'jobs': jobs})

def job_list(request):
    jobs = Job.objects.all()
    return render(request, 'job_list.html', {'jobs': jobs})


def job_search(request):
    search_title = request.GET.get('title', '')
    search_location = request.GET.get('location', 'All Locations')

    # تصفية الوظائف بناءً على معايير البحث
    jobs = Job.objects.all()

    if search_title:
        jobs = jobs.filter(title__icontains=search_title)  # البحث في العنوان
    if search_location != 'All Locations':
        jobs = jobs.filter(location__icontains=search_location)  # البحث في الموقع

    # إرجاع استجابة تحتوي على الوظائف
    return render(request, 'job_list.html', {'jobs': jobs})