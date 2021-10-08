from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy
from django.contrib.auth.models import AbstractBaseUser ,BaseUserManager, Group, PermissionsMixin
from django.contrib.auth.hashers import make_password
# Create your models here.



class CustomUserManager(BaseUserManager):

    def create_user(self,uid,name,password,**other_fields):
        
        if not uid:
            return ValueError(gettext_lazy("uid not provided"))

        if not password or len(password)<6:
            return ValueError(gettext_lazy("password should be more than 6 characters"))    

        user = self.model(uid=uid,name=name,**other_fields)

        user.set_password(password)
        user.save()

        return user


    def create_superuser(self,uid,name,password,**other_fields):
        other_fields.setdefault('is_staff',True)
        other_fields.setdefault('is_superuser',True)
        other_fields.setdefault('is_active',True)


        return self.create_user(uid,name,password,**other_fields)

    


class NewUser(AbstractBaseUser,PermissionsMixin):
    uid = models.CharField(max_length=10,unique=True)
    name = models.CharField(max_length=30,blank=True)
    email = models.EmailField(gettext_lazy('email address'),unique=True,blank=True,null=True)
    level = models.PositiveIntegerField(default=0)
    joined_date = models.DateTimeField(default=timezone.now)

    is_staff = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'uid'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name



