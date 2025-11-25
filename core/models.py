from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    USER_ROLES = (
        ('employer', 'Employer'),
        ('candidate', 'Candidate'),
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=USER_ROLES, default='candidate')
    company_name = models.CharField(max_length=200, blank=True)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f'{self.user.username} ({self.role})'
