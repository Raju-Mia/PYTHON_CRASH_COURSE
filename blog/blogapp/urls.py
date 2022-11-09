from django.urls import path

from . import views


app_name = "blogapp"

urlpatterns = [

    path('home/', views.blog, name='home'),
    path('editblog/', views.editblog, name='editblog')

]