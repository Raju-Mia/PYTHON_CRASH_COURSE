from multiprocessing import context
from django.shortcuts import render, redirect
import learning_logs

from learning_logs.models import Topic, Pizaeria, Entry
from .forms import TopicForm, EntryForm

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


def new_topic(request):

    if request.method != 'POST':
        form = TopicForm()

    else:
        form = TopicForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topics') #also can used '/topics/' for redirect page. views name is topics name.
        

    context = {'form': form}
    return render(request, "new_topic.html", context)



def new_entry(request, topic_id):
    topic = Topic.objects.get(id = topic_id)
    if request.method != 'POST':
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect("learning_logs:topic", topic_id = topic_id) 

    context = {'topic': topic, 'form': form}

    return render(request, "new_entry.html", context)



#edit_entry funtion for edit the entry details.
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic_filed = entry.topic #topic means Topic model topic field name.

    if request.method != 'POST':
        form = EntryForm(instance=entry) #Entryform is forms.py class
    
    else:
        form = EntryForm(instance=entry, data = request.POST) #Entryform is forms.py class
        if form.is_valid():
            form.save()
            return redirect('learning_logs:topic', topic_id=topic.id)

    context = {'entry': entry, 'topic':topic_filed, 'form':form}
    return render(request, 'edit_entry.html', context)
    