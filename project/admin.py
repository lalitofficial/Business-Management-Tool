from django.contrib import admin
from .models import Task,Attachment
# Register your models here.
admin.site.register(Task),
admin.site.register(Attachment)