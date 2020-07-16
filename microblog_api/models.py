from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager
from django.conf import settings
# Create your models here.
class UserProfileManager(BaseUserManager):

    def create_user(self, name, email, password = None):
        if not name:
            raise ValueError("User must have a name")

        email = self.normalize_email(email)
        user = self.model(name = name, email = email)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password):
        user = self.create_user(name, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user

class UserProfile(AbstractBaseUser, PermissionsMixin):
    """ model for users """
    name = models.CharField(max_length = 100, unique = True)
    email = models.EmailField(max_length = 200)
    is_active = models.BooleanField(default = True)
    is_staff = models.BooleanField(default = False)

    objects = UserProfileManager()

    USERNAME_FIELD = "name"
    REQUIRED_FIELDS = ["email"]

    def get_full_name(self):
        return self.name

    def get_email(self):
        return self.email

    def __str__(self):
        return str(self.name) + " " + str(self.email)


class Blog(models.Model):
    """ model for blogs """
    text = models.CharField(max_length = 300)
    likes = models.IntegerField(default = 0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "Blogs"

    def __str__(self):
        return str(self.id) + " " + str(self.user) + " " + str(self.text)

class Comment(models.Model):
    """ model for comments """
    text = models.CharField(max_length = 300)
    likes = models.IntegerField(default = 0)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete = models.CASCADE)

    class Meta:
        verbose_name_plural = "Comments"

    def __str__(self):
        return str() + " " + str(self.user) + " " + str(self.blog) + " " + str(self.text)
