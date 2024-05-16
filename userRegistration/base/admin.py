from django.contrib import admin

from . models import attendee, user

# Register your models here.
admin.site.register(user)
admin.site.register(attendee)