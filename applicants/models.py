from django.db import models
from accounts.models import User
from core.models import Skill

class ApplicantProfile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE, related_name="applicant_profile")
    resume_url=models.URLField(max_length=500,blank=True,null=True)
    skills = models.ManyToManyField(Skill, blank=True)
    
    def __str__(self):
        return self.user.username
