# Generated by Django 5.0.6 on 2024-07-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_remove_meetup_participants_meetup_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]