from django.db import models

class Member(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)

class SoloTaskManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(soloTask=True)

class Task(models.Model):
    taskName = models.CharField(max_length=100)
    taskDescription = models.TextField()
    soloTask = models.BooleanField()
    taskLocation = models.CharField(max_length=300)
    taskDate = models.DateField()

    objects = models.Manager()
    soloTasks = SoloTaskManager()
