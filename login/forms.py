from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import NewUser


class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = NewUser
        fields = ('uid','name','level','is_staff','is_active','is_superuser')


class CustomUserChangeForm(UserChangeForm):
    
    class Meta:
        model = NewUser
        fields =   ('uid','name','level','is_staff','is_active','is_superuser')
        