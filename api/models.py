from django.db import models

# Create your models here.


class User(models.Model):

    name  = models.CharField(max_length=255, default="")
    username  = models.CharField(max_length=255, default="")
    email=models.EmailField(max_length=255, default="")
    password = models.TextField(default="")


class audiofiles(models.Model):

    audio = models.FileField(upload_to='user/',default="")
    user_id = models.ForeignKey(User, on_delete=models.CASCADE,blank=True, null=True)