import json
from django.core.management.base import BaseCommand
from home.models import Job
from django.conf import settings
import os

class Command(BaseCommand):
    help = 'Load job listings from a JSON file into the database'

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, 'careers', 'job_details.json')

        with open(file_path, 'r') as f:
            data = json.load(f)
            for job in data['jobs']:
                Job.objects.create(
                    job_title=job['jobTitle'],
                    location=job['location'],
                    employment_type=job['employmentType'],
                    salary=job['salary'],
                    company=job['company'],
                    intro="\n\n".join(job['introParagraphs']),
                    responsibilities="\n".join(job['responsibilities']),
                    requirements="\n".join(job['requirements']),
                    benefits="\n".join(job['benefits']),
                    apply_link=job['links']['applyNow'],
                    all_jobs_link=job['links']['allJobs']
                )

        self.stdout.write(self.style.SUCCESS('Job data loaded successfully.'))
