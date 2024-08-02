# Generated by Django 5.0.4 on 2024-05-15 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FA', '0003_alter_invited_talks_name_of_event_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='SDP_organised',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_coord', models.CharField(max_length=1000)),
                ('type_of_event', models.CharField(max_length=100)),
                ('name_of_event', models.CharField(max_length=200)),
                ('duration', models.CharField(max_length=100)),
                ('no_of_participants', models.IntegerField()),
                ('resource_persons', models.CharField(max_length=1000)),
                ('sponsors', models.CharField(max_length=200)),
                ('academic_year', models.CharField(max_length=100)),
            ],
        ),
    ]
