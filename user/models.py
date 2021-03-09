from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class UserManager(BaseUserManager):

    def create_user(self, email, password=None):
        """
        Create and return a `User` with an email, username and password.
        """
        if not email:
            raise ValueError('Users Must Have an email address')
        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Create and return a `User` with superuser (admin) permissions.
        """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True
    )
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()


def __str__(self):
    return self.email


class Meta:
    """
    to set table name in database
    """
    db_table = "users"


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    subject = models.CharField(max_length=10, null=True, blank=True)
    standard = models.CharField(max_length=10, null=True, blank=True)
    SUPER_ADMIN = 1
    TEACHER = 2
    STUDENT = 3

    ROLE_CHOICES = (
        (SUPER_ADMIN, 'Super-admin'),
        (TEACHER, 'Teacher'),
        (STUDENT, 'Student'),
    )
    role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True)


# class StudentProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='student_profile')
#     first_name = models.CharField(max_length=50, null=True, blank=True)
#     last_name = models.CharField(max_length=50, null=True, blank=True)
#     phone_number = PhoneNumberField(blank=True, null=True, unique=True)
#     standard = models.CharField(max_length=10, null=True, blank=True)
