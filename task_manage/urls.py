from django.urls import path, include
from rest_framework.routers import DefaultRouter

from task_manage import views


router = DefaultRouter()
router.register('task', views.TaskViewSet)
router.register('comment', views.CommentTaskViewSet)

app_name = 'task'

urlpatterns = [
    path('', include(router.urls))
]