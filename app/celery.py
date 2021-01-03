from __future__ import absolute_import

from datetime import timedelta
import os
from celery import Celery
from celery.schedules import crontab
from app import settings
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

# import django
#
# django.setup()
# celery = Celery('tasks', broker=BROKER_URL)
app = Celery('app')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
# app.autodiscover_tasks()
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'get_weekly_report': {
        'task': 'weekly_report',
        # 'schedule': crontab(),
        'schedule': crontab(minute=0, hour=0, day_of_month='*', day_of_week='monday'),
        # 'schedule': timedelta(seconds=10),

    }
}
