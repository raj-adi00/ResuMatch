from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    USER_ROLES= (
        ('applicant','Applicant'),
        ('company','Company')
    )
    role=models.CharField(max_length=15,choices=USER_ROLES)
    
    def __str__(self):
        return f"{self.username} ({self.role})"
    