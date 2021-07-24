from django.contrib import admin
from .models import Password

# Register your models here.

class PasswordModel(admin.ModelAdmin):
    list_display = ('username', 'email', 'password')


admin.site.register(Password, PasswordModel)