# Generated by Django 3.1.7 on 2021-11-06 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ideathonwebapp', '0003_auto_20211106_0038'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='ageRange',
            field=models.CharField(choices=[('All Ages', 'All Ages'), ('18+', '18+'), ('21+', '21+')], max_length=10),
        ),
    ]