from django.contrib import admin

# Register your models here.
from .models import Cliente,Article

admin.site.register(Cliente)
admin.site.register(Article)