from django.db import models
import json
# Create your models here.

class Job(models.Model):
    job_title = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=100)
    salary = models.CharField(max_length=100)
    company = models.CharField(max_length=255)
    intro = models.TextField(default="Coming soon...")
    responsibilities = models.TextField()
    requirements = models.TextField()
    benefits = models.TextField()
    apply_link = models.URLField(max_length=500)
    all_jobs_link = models.URLField(max_length=500)

    def __str__(self):
        return self.job_title