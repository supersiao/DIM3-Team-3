from django import forms
from django.contrib.auth.models import User
from rango.models import UserProfile, Company, Job, Resume


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
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = UserProfile
        exclude = ['Username']


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'email', 'phone', 'nationality', 'address', 'location', 'levelEdu', 'WorkingExperience', 'userID')


class EditProfileForm(forms.ModelForm):


    class Meta:
        model = User
        fields = ('username', 'email', 'password')


class CreateJobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ('name', 'position', 'postionArea', 'companyID', 'userID' )


