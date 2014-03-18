from django.conf.urls import patterns, url
from rango import views

urlpatterns = patterns('',
	url(r'^index/$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^employer_login/$' , views.employ_login,name='employer_login'),
    url(r'^intern_login/$' , views.intern_login,name='intern_login'),
    url(r'^intern_dash/$' , views.intern_dash,name='intern_dash_board'),
    url(r'^employ_dash/$' , views.employ_dash,name='employer_dash_board'),
    url(r'^employ_edit/$' , views.employ_edit,name='employer_edit_profile'),
    url(r'^intern_edit_profile/$' , views.intern_edit_profile, name='intern_edit_profile'),
    url(r'^intern_match/$' , views.intern_match,name='intern_match'),
    url(r'^job_posting/$' , views.job_posting,name='job_postings'),
    url(r'^job_posting/$' , views.job_posting,name='job_postings'),
    url(r'^posted_job/$' , views.posted_job,name='posted_jobs'),
    url(r'^post_resume/$' , views.post_resume,name='post_resume'),
    url(r'^intern_search/$' , views.intern_search,name='intern_search'),
	url(r'^restricted/$', views.restricted, name='restricted'),

	)

