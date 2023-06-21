from django.db import models

# Create your models here.

# To modify database once models are created, run "python3 manage.py makemigrations #{name of app}"
# Then: python3 manage.py migrate to run migrations

class ToDoList(models.Model):
  name = models.CharField(max_length=200)

  def _str_(self):
    return self.name

class Item(models.Model):
  todolist = models.ForeignKey(ToDoList, on_delete=models.CASCADE)
  text = models.CharField(max_length=300)
  complete = models.BooleanField()

  def __str__(self):
    return self.text

