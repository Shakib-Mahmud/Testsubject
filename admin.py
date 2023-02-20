from django.contrib import admin
from .models import UserMaster,Author,Blog,Comment

# Register your models here.
admin.site.register(UserMaster)
admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Comment)