from django.contrib import admin
from main.models import course,logIn,register
# Register your models here.
admin.site.register(logIn)
admin.site.register(course)
admin.site.register(register)