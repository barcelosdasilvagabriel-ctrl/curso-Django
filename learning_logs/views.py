from django.shortcuts import render
from .models import Topic


# Create your views here.

def index(request):
    
    return render(request, 'learning_logs/index.html')


def topics(request):
    '''Mostra todos os assuntos'''
    
    topics = Topic.objects.order_by('date_added')
    
    contexto = {'topics':topics}
    
    return render(request,'learning_logs/topics.html',contexto)

def topic(request,topic_id):
    
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by("date_added")
    contexto = {"topic":topic,'entries':entries}
    
    return render(request,'learning_logs/topic.html',contexto)