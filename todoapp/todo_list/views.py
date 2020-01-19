from django.shortcuts import render
from .models import ToDoList
from .forms import ListForm
from django.contrib import messages

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