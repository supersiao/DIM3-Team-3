from django.contrib import admin
from rango.models import Company, Job, Resume, UserProfile


admin.site.register(Company)
admin.site.register(UserProfile)
admin.site.register(Job)
admin.site.register(Resume)