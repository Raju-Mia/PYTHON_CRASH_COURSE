from enum import auto
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Topic(models.Model):
    text = models.TextField(max_length = 200)
    date_added = models.DateTimeField(auto_now_add = True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text



class Entry(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add = True)

    class Meta:
        verbose_name_plural = 'entries'

    def __str__(self):
        return f"{self.text[:50]}..."
    
    
class Pizaeria(models.Model):
    p_name = models.CharField(max_length=200)
    p_size = models.CharField(max_length=200)
    p_quantity = models.IntegerField()
    p_details = models.TextField()


    def __str__(self):
        return self.p_name