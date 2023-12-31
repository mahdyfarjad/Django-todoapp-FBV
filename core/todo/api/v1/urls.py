from rest_framework.routers import DefaultRouter
from .views import TaskModelViewSet

app_name = 'todo-api'

router = DefaultRouter()
router.register('todo', TaskModelViewSet, basename='todo')

urlpatterns = router.urls