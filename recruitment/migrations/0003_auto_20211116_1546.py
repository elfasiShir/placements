# Generated by Django 3.2.8 on 2021-11-16 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('recruitment', '0002_auto_20211115_1000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobround',
            name='job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='job_rounds', to='recruitment.job'),
        ),
        migrations.AlterField(
            model_name='jobround',
            name='venue',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='jobround',
            unique_together={('job', 'round_number')},
        ),
    ]
