from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class UserProfile(models.Model):
    full_name = models.CharField(max_length=100, default='Unknown Address')
    email = models.EmailField(max_length=200, default='Unknown Address')
    address = models.CharField(max_length=200, default='Unknown Address')
    college_name = models.CharField(max_length=100, default='Unknown Address')
    course_name = models.CharField(max_length=100, default='Unknown Address')
    semester = models.CharField(max_length=10, default='Unknown Address')
    phone_number = models.CharField(max_length=15, default='Unknown Address')
    whatsapp_number = models.CharField(max_length=15, default='Unknown Address')
    insta_username = models.CharField(max_length=100, default='Unknown Address')
    twitter_username = models.CharField(max_length=100, default='Unknown Address')
    telegram_username = models.CharField(max_length=100, default='Unknown Address')
    DOB = models.DateField(max_length=10, default='2000-01-01')
    para = models.TextField(max_length=300, default='Uknown messages')
    college_id = models.FileField(upload_to='college_id/', default='Unknown College ID')
    file_cv = models.FileField(upload_to='cv/', default='Unknown CV')
    photo = models.FileField(upload_to='photos/', default='Unknown Photo')
    verified_doc = models.FileField(upload_to='verified_doc/', default='Unknown DOC')
    result = models.FileField(upload_to='result/', default='Unknown Result')
    declaration = models.BooleanField(default=False)
    flexRadioDefault = models.BooleanField(default=False)
    occupation = models.CharField(max_length=100, default='Unknown Address')


class Member(models.Model):
    name = models.CharField(max_length=100, default='Unknown Address')
    course = models.CharField(max_length=100, default='Unknown Address')
    college = models.CharField(max_length=100, default='Unknown Address')
    responsibility = models.CharField(max_length=100, default='Unknown Address')
    phone_number = models.CharField(max_length=15, default='Unknown Address')
    email = models.EmailField(max_length=200, default='Unknown Address')
    photo = models.ImageField(upload_to='photos/', default='Unknown Address')
        # Add a new field for ID card status
    id_card_generated = models.BooleanField(default=False)

# Dashboard Models________________________________________________________________________/\

class AdminProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_picture = models.ImageField(upload_to='profile_pictures/', blank=True, null=True)
    bio = models.TextField(blank=True)
    contact_information = models.CharField(max_length=255, blank=True)
    # Add more fields as needed


class Announcement(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Replace '1' with the ID of a default user
    title = models.CharField(max_length=200)
    description = models.TextField(default='Unknown Discription')
    created_at = models.DateTimeField(auto_now_add=True)

# class MemberProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     profile_picture = models.ImageField(upload_to='profile_pictures/', null=True, blank=True)
#     name = models.CharField(max_length=255)

#     def __str__(self):
#         return self.user.username  # Use the username as the default name for the profile
    
# @receiver(post_save, sender=User)
# def create_member_profile(sender, instance, created, **kwargs):
#     if created:
#         MemberProfile.objects.create(user=instance)

# @receiver(post_save, sender=User)
# def save_member_profile(sender, instance, **kwargs):
#     instance.memberprofile.save()
