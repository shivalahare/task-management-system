from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('member', 'Member'),
    )
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)

class Task(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    assigned_to = models.ForeignKey('CustomUser', on_delete=models.CASCADE, related_name='tasks')
    status_choices = [('todo', 'To Do'), ('inprogress', 'In Progress'), ('done', 'Done')]
    status = models.CharField(max_length=10, choices=status_choices, default='todo')

    def __str__(self):
        return self.title
