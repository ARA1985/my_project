# import datetime

from django.db import models
# from django.utils import timezone
from django.contrib import admin
from django.forms import ModelForm

# Create your models here.


class Customer(models.Model):
    name = models.CharField(max_length=200, blank=True)
    telephone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200, blank=True)
    message = models. TextField(max_length=2000, blank=True)
    created = models.DateTimeField('created')

    def __str__(self):
        return self.telephone


class CustomerForm(ModelForm):
    class Meta:
            model = Customer
            fields = ['name', 'telephone', 'email', 'message']
    # @admin.display(
    #     boolean=True,
    #     ordering='pub_date',
    #     description='Published recently?',
    # )
    # def was_published_recently(self):
    #     now = timezone.now()
    #     return now - datetime.timedelta(days=1) <= self.pub_date <= now
