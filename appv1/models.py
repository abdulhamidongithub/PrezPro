from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class Fan(models.Model):
    name = models.CharField(max_length=100)
    sinf = models.PositiveSmallIntegerField()

    def __str__(self):
        return f"{self.name}, {self.sinf}-sinf"

class Presentation(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='presentations')
    price = models.IntegerField(default=0)
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)
    korishlar_soni = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.name}, {self.added_date}"

class Darslik(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='darsliklar')
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, null=True)
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name}, {self.added_date}"
