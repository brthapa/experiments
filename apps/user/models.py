import os
from django.conf import settings
from django.contrib.auth.models import Group, Permission
from django.db import models
from django.utils.translation import gettext_lazy as _

# from apps.encryption.fields import EncryptedFileField

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ("Male", _("Male")),
        ("Female", _("Female")),
        ("Other", _("Other"))
    ]

    ROLE_CHOICES = [
        ("student", "Student"),
        ("instructor", "Instructor"),
        ("admin", "Admin"),
        ("Article Writer", "Article Writer")
    ]

    FIELD_OF_INTERESTS_CHOICES = [
        ("nea", "NEA"),
        ("Nepal Bank", "Nepal Bank"),
        ("Nepal Police", "Nepal Police"),
        ("Teacher Service Commission (TSC)", "Teacher Service Commission (TSC)")
    ]
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        related_name="profile",
        on_delete=models.CASCADE
    )
    middle_name = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(
        max_length=100, choices=GENDER_CHOICES, null=True, blank=True
    )
    phone = models.CharField(max_length=15, null=True, blank=True, unique=True)
    field_of_interests = models.CharField(
        max_length=100, choices=FIELD_OF_INTERESTS_CHOICES, null=True, blank=True
    )
    address = models.CharField(max_length=255, null=True, blank=True)
    dob = models.DateTimeField(null=True, blank=True)
    phone_number_is_verified = models.BooleanField(default=False)
    role = models.CharField(
        max_length=100, choices=ROLE_CHOICES, null=True, blank=True
    )
    experience_in_yrs = models.PositiveIntegerField(null=True, blank=True)
    profile_photo_url = models.ImageField(upload_to="user/profile/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username


class Device(models.Model):
    """
        Stores information about user devices for fcm notifications
    """
    device_id = models.CharField(max_length=100, null=True, blank=True)
    registration_id = models.TextField()
    email = models.CharField(max_length=100)


class UserRole(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, related_name="roles", on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name="roles", on_delete=models.CASCADE)
    started_at = models.DateTimeField(auto_now=True)
    ended_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return u'User: {}\'s role: {}'.format(self.user.__str__(), self.group.__str__())

    @staticmethod
    def is_active(user, group):
        return UserRole.objects.filter(user=user, group__name=group, ended_at=None).exists()