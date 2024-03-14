from django.db import models


class Equipment(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class User(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)


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
