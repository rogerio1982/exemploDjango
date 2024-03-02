from django.contrib import admin

# Register your models here.
#admin

from django.contrib import admin

from .models import *

class vendasAdmin(admin.ModelAdmin):
    list_display = ('produto')

admin.site.register(produto)
