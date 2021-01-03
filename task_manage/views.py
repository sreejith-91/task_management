import datetime

from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, mixins, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Task
from core.permissions import ISSuperUser, IsOwnerOrReadOnly
from task_manage import serializers


class TaskViewSet(viewsets.ModelViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.TaskSerializer
    queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,IsOwnerOrReadOnly)

    def get_queryset(self):
        """Retrieve the task for the authenticated user"""
        queryset = self.queryset
        if self.request.user.is_superuser:
            return queryset
        return queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        """Create a new task"""
        serializer.save(user=self.request.user)


class CommentTaskViewSet(viewsets.GenericViewSet):
    """Manage recipes in the database"""
    serializer_class = serializers.TaskCommentSerializer
    queryset = Task.objects.all()
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, ISSuperUser)

    def get_queryset(self):
        """Retrieve the task for the authenticated user"""
        queryset = self.queryset
        return queryset

    @action(methods=['POST'], detail=True, url_path='comment-task')
    def comment_task(self, request, pk=None):
        """comment a task"""
        recipe = self.get_object()
        serializer = self.get_serializer(
            recipe,
            data=request.data
        )

        if serializer.is_valid():
            serializer.save(commented_by=request.user,
                            commented_on=datetime.datetime.now())
            return Response(
                serializer.data,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )
