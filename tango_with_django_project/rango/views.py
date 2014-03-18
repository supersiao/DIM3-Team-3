from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from rango.bing_search import run_query
from django.contrib.auth.models import User
from django.shortcuts import redirect

def encode_url(str):
    return str.replace(' ', '_')
	

def decode_url(str):
    return str.replace('_', ' ')

def searchResult(request):
    context = RequestContext(request)
    return render(request, 'rango/index.html')

    #return render_to_response('rango/intern_search.html', context)
def search(request):
    if 'keyword' in request.GET:
        message = 'You searched for: %keyword' % request.GET['keyword']
    else:
        message = 'You submitted an empty form.'
    return HttpResponse(message)


def index(request):
    context = RequestContext(request)
    return render_to_response('rango/index.html', context)

def register(request):
    context = RequestContext(request)
    return render_to_response('rango/register.html', context)

def employ_login(request):
    context = RequestContext(request)
    return render_to_response('rango/employer_login.html', context)

def intern_login(request):
    context = RequestContext(request)

    if request.method == 'POST':
        username = request.POST['']

    return render_to_response('rango/intern_login.html', context)

def intern_dash(request):
    context = RequestContext(request)
    return render_to_response('rango/intern_dash_board.html', context)

def employ_dash(request):
    context = RequestContext(request)
    return render_to_response('rango/employer_dash_board.html', context)

def employ_edit(request):
    context = RequestContext(request)
    return render_to_response('rango/employer_edit_profile.html', context)

def intern_edit_profile(request):
    context = RequestContext(request)
    return render_to_response('rango/intern_edit_profile.html', context)

def intern_match(request):
    context = RequestContext(request)
    return render_to_response('rango/intern_match.html', context)

def job_posting(request):
    context = RequestContext(request)
    return render_to_response('rango/job_postings.html', context)

def posted_job(request):
    context = RequestContext(request)
    return render_to_response('rango/posted_jobs.html', context)

def post_resume(request):
    context = RequestContext(request)
    return render_to_response('rango/post_resume.html', context)

def intern_search(request):
    context = RequestContext(request)
    return render_to_response('rango/intern_search.html', context)

def restricted(request):
    context = RequestContext(request)
    return render_to_response('rango/restricted.html', context)

