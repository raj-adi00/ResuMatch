from django.db import models
from accounts.models import User
from jobs.models import JobPost

class Application(models.Model):
    applicant = models.ForeignKey(User, on_delete=models.CASCADE, limit_choices_to={'role':'applicant'})
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE)
    applied_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[
            ('applied','Applied'),
            ('reviewed','Reviewed'),
            ('accepted','Accepted'),
            ('rejected','Rejected')
        ],
        default='applied'
    )

    class Meta:
        unique_together = ('applicant','job')  # prevent multiple applications

    def __str__(self):
        return f"{self.applicant.username} → {self.job.title}"
