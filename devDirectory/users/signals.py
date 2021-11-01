from django.db.models.signals import post_save,post_delete
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.conf import settings
from .models import Profile

# signals notifiers
# @receiver(post_save,sender=Profile)
# For new user
def createProfile(sender,instance,created,**kwargs):

    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
            email=user.email,
            name=user.first_name
            )
        subject = 'Welcome to TalentMine!'
        message = 'Welcome to the TalentMine!,We at TalentMine are trying to make largest group of talented individuals to give them a platform to showcase there skills and get hired.'
        send_mail(
            subject,
            message,
            settings.EMAIL_HOST_USER,
            [profile.email], 
            fail_silently=False,
        )


def updateUser(sender,instance,created,**kwargs):
    profile = instance
    user = profile.user
    if created == False:
        user.first_name = profile.name
        user.username = profile.name
        user.email = profile.name
        user.save()



# For deleted user
def deleteUser(sender,instance,**kwargs):
    user = instance.user
    user.delete()


post_save.connect(createProfile,sender=User)
post_save.connect(updateUser,sender=Profile)
post_delete.connect(deleteUser,sender=Profile)
