
from django.urls import path
from . import views

app_name = "learning_logs"

urlpatterns = [
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name='topics'),
    #details page for a signle topic
    path('topics/<int:topic_id>/', views.topic,  name='topic'),
    path('piza/',views.pizaeria, name="pizaeria"),

    #forms url
    path('new_topic/', views.new_topic, name="new_topic"),
    path('new_entry/<int:topic_id>/', views.new_entry, name="new_entry"),

    #entry details edit url
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
]