from django.apps import AppConfig


class TaskConfig(AppConfig):
    name = 'task_manage'

    def ready(self):
        import task_manage.signals
