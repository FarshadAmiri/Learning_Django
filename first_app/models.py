from django.db import models

class User(models.Model):
    GENDER_CHOICES = (('m','male'), ('f','female'))
    name = models.CharField(max_length=70)
    age = models.IntegerField()
    gender = models.CharField(choices=GENDER_CHOICES, default='m', max_length=15)
    country = models.CharField(max_length=50)
    email = models.EmailField()
    username = models.CharField(max_length=20)
    signing_date = models.DateField()

class Post(models.Model):
    content = models.TextField(blank=False, null=False, max_length=200)
    writer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

# Create your models here.
