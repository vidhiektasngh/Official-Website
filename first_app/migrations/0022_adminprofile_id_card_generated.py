# Generated by Django 4.2.6 on 2023-11-05 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0021_adminprofile_bio_adminprofile_contact_information_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminprofile',
            name='id_card_generated',
            field=models.BooleanField(default=False),
        ),
    ]