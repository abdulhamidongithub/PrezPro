from django.db import models
from django.contrib.auth.models import AbstractUser

GURUH_CHOICE = (
    ("o'zbek", "o'zbek"),
    ("rus", "rus")
)

class CustomUser(AbstractUser):
    phone = models.CharField(max_length=30)
    birth_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username

class Fan(models.Model):
    name = models.CharField(max_length=100)
    sinf = models.PositiveSmallIntegerField()
    guruh = models.CharField(max_length=10, default="o'zbek", choices=GURUH_CHOICE)

    def __str__(self):
        return f"{self.name}, {self.sinf}-sinf"

class Presentation(models.Model):
    name = models.CharField(max_length=300, blank=True, null=True)
    file = models.FileField(upload_to='presentations')
    price = models.IntegerField(default=0)
    chorak = models.PositiveSmallIntegerField(default=1)
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

class IshReja(models.Model):
    file = models.FileField(upload_to='ish_rejalar')
    fan = models.ForeignKey(Fan, on_delete=models.SET_NULL, null=True)
    chorak = models.PositiveSmallIntegerField(default=1)
    added_by = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    added_date = models.DateTimeField(auto_now_add=True)
    changed_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.fan.name} ({self.fan.sinf}-sinf), {self.chorak}-chorak"
