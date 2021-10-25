from django.db import models
from django.contrib.auth.models import User
import uuid
# Create your models here.

class Profiles(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length = 100,blank=True,null=True)
    email = models.EmailField(max_length=100,blank=True,null=True)
    short_intro  = models.CharField(max_length = 180,blank=True,null=True)
    bio = models.TextField(blank=True,null=True)
    profile_image = models.ImageField(null=True,blank=True,upload_to = 'profiles/',default ="profiles/avatar.jpeg" )
    social_github =  models.CharField(max_length = 5000,blank=True,null=True)
    social_twitter =  models.CharField(max_length = 5000,blank=True,null=True)
    social_linkedin =  models.CharField(max_length = 5000,blank=True,null=True)
    social_website =  models.CharField(max_length = 5000,blank=True,null=True)
    social_email =  models.CharField(max_length = 5000,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return str(self.user.name)