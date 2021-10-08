
from django.contrib.auth.admin import UserAdmin
from django.contrib import admin
from django.contrib.auth.models import User
from .models import NewUser
from .forms import CustomUserChangeForm, CustomUserCreationForm
# Register your models here.

class CustomUserAdmin(UserAdmin):
    
    add_form  = CustomUserCreationForm
    form = CustomUserChangeForm
    model = NewUser

    list_display =  ('uid','name','level','is_staff','is_active','is_superuser')
    list_filter =  ('uid','name','level','is_staff','is_active','is_superuser')
    fieldsets = (
        (None,{'fields':('uid','password','name','level',"groups")}),
        ('Permissions',{'fields':('is_staff','is_active')}),
    )

    add_fieldsets = (
        (
            None,
            {
                'classes':('wide'),
                'fields':('uid','name','password1','password2','is_staff','is_active','is_superuser'),
            }
        ),
        (
            'Group Permissions',{
                'classes':('collapse',),
                'fields':('groups',)
            }
        ),
    )

    search_fields =  ('uid','name')
    ordering =  ('name',)

admin.site.register(NewUser,CustomUserAdmin)

