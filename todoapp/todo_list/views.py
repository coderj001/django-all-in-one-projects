from django.shortcuts import render, redirect
from .models import ToDoList
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

# Create your views here.
def home(req):
	if req.method=='POST':
		form=ListForm(req.POST or None)
		if form.is_valid():
			form.save()
			all_items=ToDoList.objects.all
			messages.success(req,('item has been added!'))
			return render(req, 'home.html', {'items':all_items})
	else:
		all_items=ToDoList.objects.all
		return render(req, 'home.html', {'items':all_items})
def about(req):
	return render(req, 'about.html',{})
def delete(req,list_id):
	item=ToDoList.objects.get(pk=list_id)
	item.delete()
	messages.success(req,('item has been delete!'))
	return redirect('home')
def cross_off(req,list_id):
	item=ToDoList.objects.get(pk=list_id)
	item.completed=True
	item.save()
	return redirect('home')
def uncross(req,list_id):
	item=ToDoList.objects.get(pk=list_id)
	item.completed=False
	item.save()
	return redirect('home')
def edit(req,list_id):
	if req.method=='POST':
		item=ToDoList.objects.get(pk=list_id)
		form=ListForm(req.POST or None, instance=item)
		if form.is_valid():
			form.save()
			messages.success(req,('item has been edited!'))
			return redirect('home')
	else:
		item=ToDoList.objects.get(pk=list_id)
		return render(req, 'edit.html', {'item':item})