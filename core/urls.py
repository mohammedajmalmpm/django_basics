from django.urls import path
from core.views import home,task,delete, update
urlpatterns = [
    path("", home , name="home"),
    path('task', task, name = "task"),
    path('update/<todo_id>/',update, name = 'update'),
    path('delete/<todo_id>/',delete, name = 'delete')
]
