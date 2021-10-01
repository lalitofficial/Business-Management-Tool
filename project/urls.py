from django.urls import path
from project import views

urlpatterns = [
    path('',views.project,name="project"),
    path('task/',views.task,name="task"),
    path('d/',views.detail_task,name="detail_task")
]