# Generated by Django 5.0.6 on 2024-05-21 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0005_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='duration',
            field=models.CharField(max_length=100),
        ),
    ]
