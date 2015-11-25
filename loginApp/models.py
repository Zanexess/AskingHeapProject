from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyUserManager(BaseUserManager):
    def create_user(self, username=None, email=None, first_name=None, last_name=None,
                    middle_name=None, rate=None, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model( username=username,
                        email=MyUserManager.normalize_email(email),
                        first_name=first_name,
                        middle_name=middle_name,
                        last_name=last_name,
                        rate=rate,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password, first_name=None, last_name=None,
                    middle_name=None, rate=None,):
        user = self.create_user(username, email,
            password=password,
            first_name=username,
            last_name=username,
            middle_name=username, rate=0,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.set_password(password)

        user.save(using=self._db)
        return user



