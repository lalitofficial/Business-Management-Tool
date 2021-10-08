from django.urls import path
from django.urls.resolvers import URLPattern
from login import views

urlpatterns = [ 

    path('',views.user_login,name="login")

]