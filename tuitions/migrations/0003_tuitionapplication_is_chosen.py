# Generated by Django 4.2.9 on 2024-01-18 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0002_tuition_days_per_week_tuition_gender_tuition_grade_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tuitionapplication',
            name='is_chosen',
            field=models.BooleanField(default=False),
        ),
    ]
