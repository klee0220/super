from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    groups = models.ManyToManyField(Group, related_name='custom_users_groups')
    user_permissions = models.ManyToManyField(Permission, related_name='custom_users_permissions')


class Equipment(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class CustomUserManager(models.Manager):
    pass


class FieldAnalyzer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=50)


class Request(models.Model):
    request_type = models.CharField(max_length=100)
    urgency = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    last_updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    analyzer = models.ForeignKey(FieldAnalyzer, on_delete=models.CASCADE)

    def mark_as_completed(self):
        self.status = 'Completed'
        self.save()

    def mark_as_in_progress(self):
        self.status = 'In Progress'
        self.save()
