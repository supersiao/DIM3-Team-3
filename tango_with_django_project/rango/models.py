from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    Username = models.OneToOneField(User, unique=True)
    email = models.CharField(max_length=100)
    role = models.CharField(max_length=40)


class Company (models.Model):
    companyName = models.CharField(max_length=128)
    website = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __unicode__(self):
         return self.companyName


class Job (models.Model):
    name = models.CharField(max_length=50)
    position = models.CharField(max_length=50)
    postionArea = models.CharField(max_length=50)
    companyID = models.ForeignKey(Company)
    userID = models.ForeignKey(User)

    def __unicode__(self):
         return self.name


class Resume(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    worksExperience = models.CharField(max_length=200)
    location = models.CharField(max_length=50)
    salary = models.PositiveIntegerField(max_length=10)
    nationality = models.CharField(max_length=20)
    userID = models.ForeignKey(User)

    def __unicode__(self):
         return self.name