from django.contrib import admin

from home.models import projects, resume, edu, exp

# Register your models here.
admin.site.register(projects)
admin.site.register(resume)
admin.site.register(edu)
admin.site.register(exp)