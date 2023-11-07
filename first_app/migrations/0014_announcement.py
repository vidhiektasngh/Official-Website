# Generated by Django 4.2.6 on 2023-11-03 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first_app', '0013_delete_dashboard'),
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('content', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]