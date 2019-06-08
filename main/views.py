from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoItem
# Create your views here.

def index(request):
    todo_item = TodoItem.objects.all()
    context = {
        'all_todo_item' : todo_item
    }
    return render(request,'index.html',context)

def addtodo(request):
    new_item = TodoItem(content = request.POST['content'])
    new_item.save()
    return HttpResponseRedirect('/')

def deletetodo(request,pk):
    delete_item = TodoItem.objects.get(id=pk)
    delete_item.delete()
    return HttpResponseRedirect('/')