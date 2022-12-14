from multiprocessing import context
from django.shortcuts import render
import learning_logs

from learning_logs.models import Topic, Pizaeria


# Create your views here.

def index(request):
    return render(request, 'index.html')


def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'topics.html', context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries':entries}
    return render(request, 'topic.html',context)


def pizaeria(request):
    name = Pizaeria.objects.filter()
    context ={'piza': name }
    return render(request, "pizaeria.html", context)
