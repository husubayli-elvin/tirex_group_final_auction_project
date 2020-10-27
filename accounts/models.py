from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    GENDER_CHOICES =(
        ("Male", ("Male")),
        ("Female", ("Female"))
    )

    image = models.ImageField(upload_to='images')
    gender = models.CharField(choices=GENDER_CHOICES, max_length=6)
    email = models.EmailField(('email adress'), unique=True, null=True)
    # Level model relationship here
    last_level_updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
