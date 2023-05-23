from django.shortcuts import render,redirect
from django.views.generic import View
from tasks.models import Todo

from django import forms



class TodoForm(forms.Form):
    task_name=forms.CharField()
    user=forms.CharField()

class TodoCreateView(View):
    
    def get(self,request,*args,**kwargs):
        form=TodoForm()
        return render(request,"todo-add.html",{"form":form})
    
    
    def post(self,request,*args,**kwargs):
        form=TodoForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            Todo.objects.create(**form.cleaned_data)
            return redirect("todo-list")
        return render(request,"todo-add.html",{"form":form})
    
class TodoListView(View):
    def get(self,request,*args,**kw):
        qs=Todo.objects.all()
    
        return render(request,"todo-list.html",{"todo":qs})
    
class TodoDetailView(View):

    def get(self,request,*args,**kwargs):
        print(kwargs)
        id=kwargs.get("pk")
        qs=Todo.objects.get(id=id)
        return render(request,"todo-detail.html",{"todo":qs})