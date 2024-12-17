from django.contrib import admin
from .models import CustomUser, Todo

admin.site.register(CustomUser)

admin.site.register(Todo)