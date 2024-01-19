# Generated by Django 4.2.9 on 2024-01-19 03:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tuitions', '0006_alter_tuition_grade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tuition',
            name='grade',
            field=models.CharField(choices=[('Class 1', 'Class 1'), ('Class 2', 'Class 2'), ('Class 3', 'Class 3'), ('Class 4', 'Class 4'), ('Class 5', 'Class 5'), ('Class 6', 'Class 6'), ('Class 7', 'Class 7'), ('Class 8', 'Class 8'), ('Class 9', 'Class 9'), ('Class 10', 'Class 10'), ('Class 11', 'Class 11'), ('Class 12', 'Class 12'), ('Admission Test', 'Admission Test'), ('IELTS', 'IELTS'), ('BCS & Job Test', 'BCS & Job Test')], max_length=200, verbose_name='Class'),
        ),
    ]