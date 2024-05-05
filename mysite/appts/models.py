from django.db import models
from django.contrib.auth.models import User


class Topic(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='appointments')
    student = models.ForeignKey('main.Student', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    occurred = models.DateTimeField()
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    note = models.TextField(blank=True)

    def __str__(self):
        return f"{self.student} -- {self.occurred}"
