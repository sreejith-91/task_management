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

# app.conf.beat_schedule = {
#     'get_nearing_deadlines': {
#         'task': 'nearing_deadlines',
#         # 'schedule': crontab(),
#         'schedule': crontab(minute=0, hour=9, day_of_month='*', day_of_week='*'),
#         # 'schedule': timedelta(seconds=10),
#
#     },
#     'clear_bulk_asset': {
#             'task': 'clear_temp_bulk_asset',
#             # 'schedule': crontab(),
#             'schedule': crontab(minute=0, hour=12, day_of_month='*', day_of_week='*'),
#             # 'schedule': timedelta(seconds=10),
#
#         },
#     'add_asset_to_shopify': {
#             'task': 'add_asset_to_shopify',
#             # 'schedule': crontab(),
#             'schedule': crontab(minute=0, hour=3, day_of_month='*', day_of_week='*'),
#             # 'schedule': timedelta(seconds=10),
#
#         },
#     'create_payslips': {
#         'task': 'create_payslips',
#         'schedule': crontab(minute='*/5')
#         # 'schedule': crontab(hour=18)
#     }
# }
