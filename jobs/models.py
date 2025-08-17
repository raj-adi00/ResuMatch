from django.db import models
from accounts.models import User

class JobPost(models.Model):
    company = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'company'})
    title = models.CharField(max_length=255)
    description = models.TextField()
    required_skills = models.ManyToManyField('core.Skill', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.company.username}"
