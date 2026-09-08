from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class Task(models.Model):
    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField()
    soloTask = models.BooleanField()
    taskLocation = models.CharField(max_length=300)
    taskDate = models.DateField()