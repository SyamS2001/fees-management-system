# Generated by Django 5.0.6 on 2024-05-21 06:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fees', '0004_qualification'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('master_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='fees.master')),
                ('Coursename', models.CharField(max_length=100)),
                ('coursecode', models.CharField(max_length=15)),
                ('amount', models.CharField(max_length=10)),
                ('duration', models.DurationField(max_length=100)),
            ],
            bases=('fees.master',),
        ),
    ]