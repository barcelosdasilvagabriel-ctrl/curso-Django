from django.shortcuts import render
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import HttpResponseRedirect
from django.urls import reverse



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


def new_topic(request):
    
    if request.method != 'POST':
        form = TopicForm()
        
    else :
        
        form = TopicForm(request.POST)    
    
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topics'))
    
    
    
    contexto = {'form':form}
    return render(request,'learning_logs/new_topic.html',contexto)
    
    
def delete_topic(request,topic_id):
    if request.method != 'POST':
        topico = Topic.objects.get(id=topic_id)
    else:
        topico = Topic.objects.get(id=topic_id)
        topico.delete()
        return HttpResponseRedirect(reverse('topics'))
    
    context = {"topic":topico}
    return render(request,"learning_logs/delete_topic.html",context)

def new_entry(request,topic_id):
    topic = Topic.objects.get(id=topic_id)
    
    if request.method != 'POST':
        form = EntryForm()
        
    else:
        form = EntryForm(data=request.POST)
    
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('topic',args=[topic_id]))
    
    context = {"topic":topic,'form':form}
    return render(request,'learning_logs/new_entry.html',context)

def edit_entry(request,entry_id):
    
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic
    
    if request.method != 'POST':
        form = EntryForm(instance=entry)
    
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('topic',args=[topic.id]))
        
    context = {"entry":entry,'topic':topic,'form':form}
    return render(request,'learning_logs/edit_entry.html',context)