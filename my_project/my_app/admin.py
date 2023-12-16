from django.contrib import admin
from django.contrib.admin import site

from .models import Article

admin.site.register(Article)
