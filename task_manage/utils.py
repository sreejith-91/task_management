import datetime
import os

import xlwt

from core.email import send_email
from core.models import Task


def create_reports():
    end_date = datetime.datetime.today().date()
    start_date = end_date - datetime.timedelta(days=7)
    task_detail = Task.objects.filter(start_date__date__range=[start_date, end_date])
    destination = "reports/"
    file_name = f"{destination}weekly_task_report" + str(datetime.datetime.today()) + ".xls"
    wb = xlwt.Workbook()
    report_sheet = wb.add_sheet('Weekly Report')
    report_sheet.write(0, 0, 'Employee Name')
    report_sheet.write(0, 1, 'Task Name')
    report_sheet.write(0, 2, 'Task Detail')
    report_sheet.write(0, 3, 'Date')
    report_sheet.write(0, 4, 'Time Required')
    x = 1
    for task in task_detail:
        report_sheet.write(x, 0, task.user.name)
        report_sheet.write(x, 1, task.name)
        report_sheet.write(x, 2, task.description)
        report_sheet.write(x, 3, task.start_date.strftime("%Y%m%d %I:%M %p"))
        report_sheet.write(x, 4, task.time_required)
        x += 1
    wb.save(file_name)
    file_path = os.getcwd() + '/' + file_name
    subject = f"Weekly report from {start_date} - {end_date}"
    message = f"Please find the attached report"
    send_email(subject=subject, message=message, attach_link=file_path)
