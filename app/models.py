from django.db import models

# Create your models here.

class My_skills(models.Model):
    title=models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to="media/app", null=True)
    def __str__(self):
        return self.title

class My_skills2(models.Model):
    title=models.CharField(max_length=100, null=True)
    img = models.ImageField(upload_to="media/app", null=True)
    def __str__(self):
        return self.title
class my_service(models.Model):
    icon=models.ImageField(upload_to="media/app", null=True)
    title = models.CharField(max_length=100, null=True)
    caption = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=100, null=True)
    btn = models.CharField(max_length=100, null=True)
    def __str__(self):
        return self.title

class Future_plane(models.Model):
    icon = models.ImageField(upload_to="media/app", null=True)
    title = models.CharField(max_length=100, null=True)
    desc = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title

class Why_trust(models.Model):
    img = models.ImageField(upload_to="media/app", null=True)
    title = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.title
