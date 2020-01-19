from django.db import models

# Create your models here.

class ToDoList(models.Model):
	item=models.CharField(max_length=200)
	completed=models.BooleanField(default=False)

	