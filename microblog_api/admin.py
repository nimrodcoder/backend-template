from django.contrib import admin
from microblog_api import models

# Register your models here.

admin.site.register(models.UserProfile)
admin.site.register(models.Blog)
admin.site.register(models.Comment)
