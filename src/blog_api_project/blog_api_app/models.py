from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager


# Create User Manager models
class UserProfileManager(BaseUserManager):
    # Helps Django to work with customized user models

    def create_user(self, email, name, password=None):
        # Create a new user profile object

        # if email is not provided
        if not email:
            raise ValueError("A user must have an email address")

        # lowercase email text
        email = self.normalize_email(email)

        # create a new user with no password
        user = self.model(email=email, name=name)

        # use set_password to encrypt password and store it in db
        user.set_password(password)

        # save new user into db
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        # Create super user with customized user models

        user = self.create_user(email, name, password)

        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)

# Create User Profile Models to override AbstractBaseUser
class UserProfile(AbstractBaseUser, PermissionsMixin):
    # Represent User Profile in Database

    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.email

    def get_full_name(self):
        # Retrieve user's get_full_name
        return self.name

    def get_short_name(self):
        # Retrieve user's short NAME
        return self.name
