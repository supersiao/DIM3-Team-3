from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Company, Job, Resume
from django.contrib.auth.forms import PasswordResetForm

class UserPasswordResetForm(PasswordResetForm):
    username = forms.CharField()

class CreateJobForm(forms.ModelForm):
        class Meta:
            model = Job
            fields = ('name', 'position', 'postionArea', 'companyID', 'userID' )

class UserForm(forms.ModelForm):
    username = forms.CharField(help_text="Please enter a username.")
    email = forms.CharField(help_text="Please enter your email.")
    password = forms.CharField(widget=forms.PasswordInput(), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
    ROLE_CHOICES = (

        (1, 'Intern'), (2, 'Employer'), (3, 'Agent'),
    )
    firstName = forms.CharField(help_text="Please enter first name.")
    lastName = forms.CharField(help_text="Please enter last name")
    address = forms.CharField(help_text="Please enter address")
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = UserProfile
       # fields = ('firstName', 'lastName', 'address')
        exclude = ['Username']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = (
        'name', 'email', 'phone', 'nationality', 'address', 'location', 'levelEdu', 'WorkingExperience', 'userID')


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'address',)

class EditEmployProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'address',)
