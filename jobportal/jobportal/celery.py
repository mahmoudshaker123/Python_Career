from __future__ import absolute_import, unicode_literals
import os
from celery import Celery

# تعيين إعدادات Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')

# إنشاء تطبيق Celery
app = Celery('jobportal')

# استخدام إعدادات Django
app.config_from_object('django.conf:settings', namespace='CELERY')

# تحميل المهام من التطبيقات المتاحة
app.autodiscover_tasks()
