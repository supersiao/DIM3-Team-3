from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.core.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from rango.forms import UserForm, UserProfileForm, CreatePostForm, EditProfileForm, CreateJobForm, EditEmployProfileForm
from datetime import datetime
from rango.bing_search import run_query
from django.contrib.auth.models import User
from rango.models import UserProfile
from rango.models import Company
from rango.models import Job
from rango.models import Resume
from django.shortcuts import redirect
from django.contrib import messages
from django import forms
from django.contrib.auth import authenticate, login as auth_login
from django.contrib.auth.views import password_reset, password_reset_confirm
from rango.forms import UserPasswordResetForm
from django.core.urlresolvers import reverse

def encode_url(str):
    return str.replace(' ', '_')


def decode_url(str):
    return str.replace('_', ' ')

def search(request):
    context = RequestContext(request)
    if request.method == 'POST':
        keyword = request.POST['keyword']
        search = request.POST['search']
        if keyword is None or keyword == "":
            return render_to_response('searchResult.html', {'keyword': Job.objects.all()}, context)
        else:
            if search == "position":
                return render_to_response('searchResult.html', {'keyword': Job.objects.filter(position = keyword)}, context)
            elif search == "PostionArea":
                return render_to_response('searchResult.html', {'keyword': Job.objects.filter(postionArea = keyword)}, context)
            elif search == "CompanyID":
                return render_to_response('searchResult.html', {'keyword': Job.objects.filter(companyID = keyword)}, context)
            elif search == "Employer":
                return render_to_response('searchResult.html', {'keyword': Job.objects.filter(userID = keyword)}, context)
            elif search == "Name":
                return render_to_response('searchResult.html', {'keyword': Job.objects.filter(name = keyword)}, context)
    return render_to_response('searchResult.html')

def internSearch(request):
    context = RequestContext(request)
    if request.method == 'POST':
        test=request.POST.getlist("test")
        return render_to_response('searchResult1.html', {'test': Job.objects.filter(postionArea = test)}, context)


def index(request):
    context = RequestContext(request)
    return render_to_response('index.html', context)


def login(request):
    context = RequestContext(request)
    return render_to_response('login.html', {}, context)


def register(request):
    # Request the context.
    context = RequestContext(request)

    # Boolean telling us whether registration was successful or not.
    # Initially False; presume it was a failure until proven otherwise!
    registered = False

    # If HTTP POST, we wish to process form data and create an account.
    if request.method == 'POST':
        # Grab raw form data - making use of both FormModels.
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)


        # Two valid forms?
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data. That one is easy.
            user = user_form.save()

            # Now a user account exists, we hash the password with the set_password() method.
            # Then we can update the account with .save().
            user.set_password(user.password)
            user.save()

            # Now we can sort out the UserProfile instance.
            # We'll be setting values for the instance ourselves, so commit=False prevents Django from saving the instance automatically.
            profile = profile_form.save(commit=False)
            profile.Username = user
            profile.save();

            # We can say registration was successful.
            registered = True

        # Invalid form(s) - just print errors to the terminal.
        else:
            print user_form.errors, profile_form.errors

    # Not a HTTP POST, so we render the two ModelForms to allow a user to input their data.
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()


        # Render and return!
    return render_to_response(
        'register.html',
        {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}, context)

def employer_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['employUsername']
        password = request.POST['employPassword']

        user = authenticate(username=username, password=password)

        if user is not None:
            if user.is_active:
                auth_login(request, user)
                request.session['sessionUsername'] = username

                return HttpResponseRedirect('../employ_dash/')
            else:
                return HttpResponse("Your Rango account is disabled.")
        else:
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied")
    else:
        return render_to_response('rango/employer_login.html', context)

def reset(request):
    return password_reset(request, template_name='rango/reset.html',
                          email_template_name='rango/reset_email.html',
                          subject_template_name='rango/reset_subject.txt',
                          password_reset_form=UserPasswordResetForm,
                          post_reset_redirect=reverse(success))

def success(request):
    return render(request, 'rango/success.html')

def reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, uidb64=uidb64, token=token,
                                  template_name='rango/reset_confirm.html',
                                   post_reset_redirect=reverse(employer_login))


def employ_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['employUsername']
        password = request.POST['employPassword']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                auth_login(request, user)
                request.session['sessionUsername'] = username

                return HttpResponseRedirect('../employ_dash/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('employer_login.html', context)


def intern_login(request):
    # Request the context of the request.
    context = RequestContext(request)
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['internUsername']
        password = request.POST['internPassword']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user is not None:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                auth_login(request, user)
                request.session['sessionUsername'] = username

                return HttpResponseRedirect('../intern_dash/')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print "Invalid login details: {0}, {1}".format(username, password)
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...

        return render_to_response('intern_login.html', context)


@login_required
def intern_dash(request):
    context = RequestContext(request)
    return render_to_response('intern_dash_board.html', context)


@login_required
def employ_dash(request):
    context = RequestContext(request)
    return render_to_response('employer_dash_board.html', context)


@login_required
def employ_edit(request):
    context = RequestContext(request)
    context = RequestContext(request)
    session = request.session['sessionUsername']
    user = User.objects.get(username=session).pk
    userProfile = UserProfile.objects.get(Username=user)

    if request.method == 'POST':
        form = EditEmployProfileForm(request.POST, instance=userProfile)
        if form.is_valid():
            form.save();

            return redirect('/rango/employ_dash')
        else:
             print form.errors
    else:
        form = EditEmployProfileForm(initial={'firstName':UserProfile.objects.filter(Username=user).get().firstName, 'lastName':UserProfile.objects.filter(Username=user).get().lastName, 'address':UserProfile.objects.filter(Username=user).get().address})
    return render_to_response('employer_edit_profile.html', {'form':form},context)



@login_required
def intern_edit_profile(request):
    context = RequestContext(request)
    session = request.session['sessionUsername']
    user = User.objects.get(username=session).pk
    userProfile = UserProfile.objects.get(Username=user)

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=userProfile)
        if form.is_valid():
            form.save();

            return redirect('/rango/intern_dash')
        else:
             print form.errors
    else:
        form = EditProfileForm(initial={'firstName':UserProfile.objects.filter(Username=user).get().firstName, 'lastName':UserProfile.objects.filter(Username=user).get().lastName, 'address':UserProfile.objects.filter(Username=user).get().address})
    return render_to_response('intern_edit_profile.html', {'form':form},context)


@login_required
def intern_match(request):
    context = RequestContext(request)
    return render_to_response('intern_match.html', context)


def job_posting(request):
    context = RequestContext(request)

    session = request.session['sessionUsername']
    user = User.objects.get(username=session).pk
    userProfile = UserProfile.objects.get(Username=user).pk

    if request.method == 'POST':
        form = CreateJobForm(data=request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/rango/intern_dash')
        else:
            print form.errors

    else:
        form = CreateJobForm()

    return render_to_response('job_postings.html', {'form': form}, context)


def posted_job(request):
    context = RequestContext(request)
    return render_to_response('posted_jobs.html', context)


@login_required
def post_resume(request):
    context = RequestContext(request)

    session = request.session['sessionUsername']
    user = User.objects.get(username=session).pk
    userProfile = UserProfile.objects.get(Username=user).pk

    if request.method == 'POST':
        form = CreatePostForm(data=request.POST)

        if form.is_valid():
            form.save(commit=True)

            return redirect('/rango/intern_dash')
        else:
            print form.errors

    else:
        form = CreatePostForm()

    return render_to_response('post_resume.html', {'form': form}, context)


def intern_search(request):
    context = RequestContext(request)
    return render_to_response('intern_search.html', context)


def restricted(request):
    context = RequestContext(request)
    return render_to_response('restricted.html', context)

