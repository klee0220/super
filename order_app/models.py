from django.db import models


class Equipment(models.Model):
    manufacturer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)


class CustomUserManager(models.Manager):
    pass


class CustomUser(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)

    objects = CustomUserManager()


class FieldAnalyzer(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Использовал переименованную модель CustomUser
    status = models.CharField(max_length=50)


class Request(models.Model):
    request_type = models.CharField(max_length=100)
    urgency = models.CharField(max_length=50)
    creation_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50)
    last_updated_date = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Использовал переименованную модель CustomUser
    analyzer = models.ForeignKey(FieldAnalyzer, on_delete=models.CASCADE)

    def mark_as_completed(self):  # Переместил метод в модель FieldAnalyzer
        self.status = 'Completed'
        self.save()

    def mark_as_in_progress(self):  # Переместил метод в модель FieldAnalyzer
        self.status = 'In Progress'
        self.save()
