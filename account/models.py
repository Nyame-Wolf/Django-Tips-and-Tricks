from django.db import models
from django.contrib.auth.models import AbstractUser

# As recommended by django docs, we use custom user.


class CustomUser(AbstractUser):
    pass
