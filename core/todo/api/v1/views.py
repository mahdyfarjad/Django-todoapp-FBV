from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from todo.models import Task
from .serializers import TaskSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .paginations import DefaultPagination

class TaskModelViewSet(viewsets.ModelViewSet):
    """ A ModelViewSet for Task """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['title', 'complete']
    search_fields = {'title':'in',}
    ordering_fields = ['title', 'complete', 'created_date']
    pagination_class = DefaultPagination