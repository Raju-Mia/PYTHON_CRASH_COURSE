from django.urls import path

from . import views


app_name = "blogapp"

urlpatterns = [

    path('home/', views.blog, name='home'),
    path('blogpost/', views.blogpost, name='blogpost'),
    path('editblog/<int:blog_id>/', views.editblog, name = 'editblog'),

]