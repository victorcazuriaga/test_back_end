from django.db import models
from django.contrib.auth.models import AbstractBaseUser
import uuid
# Create your models here.


class User(AbstractBaseUser):
    id = models.UUIDField(default=uuid.uuid4(),
                          primary_key=True, editable=False)
