from django.db import models
from django.contrib.auth.models import User


ROLE_CHOICES = (

    (1, 'Intern'), (2, 'Employer'), (3, 'Agent'),

)


class UserProfile(models.Model):
    Username = models.OneToOneField(User, unique=True)
    role = models.IntegerField(choices=ROLE_CHOICES, default=1)

    def __unicode__(self):
        return unicode(self.Username)


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

#chamge the database table and import new data. ask yee keng about edit functiona and create function
class Resume(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    phone = models.IntegerField(max_length=20)
    nationality = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    location = models.CharField(max_length=50)
    levelEdu = models.CharField(max_length=10)
    WorkingExperience = models.CharField(max_length=1000)
    userID = models.ForeignKey(User)

    def __unicode__(self):
         return self.name