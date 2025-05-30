# Generated by Django 5.1.2 on 2025-05-27 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='job',
            name='intro_paragraphs',
        ),
        migrations.AddField(
            model_name='job',
            name='intro',
            field=models.TextField(default='Coming soon...'),
        ),
        migrations.AlterField(
            model_name='job',
            name='all_jobs_link',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='apply_link',
            field=models.URLField(max_length=500),
        ),
        migrations.AlterField(
            model_name='job',
            name='benefits',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='company',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='employment_type',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='job',
            name='job_title',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='location',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='job',
            name='requirements',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='responsibilities',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='job',
            name='salary',
            field=models.CharField(max_length=100),
        ),
    ]
