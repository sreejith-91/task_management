from __future__ import absolute_import, unicode_literals
import celery

from app.celery import app
from task_manage.utils import create_reports


@app.task(name="weekly_report")
def get_weekly_report():
    create_reports()

