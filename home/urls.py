from django.urls import path
from home import views

urlpatterns = [
    
    path('',views.index,name="index"),
    path('teams/',views.teams,name="teams")
    
]