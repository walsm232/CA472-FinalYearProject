from django.db.models.signals import post_save, pre_delete
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import UserProfile, Friendship

# Receiver signal is used to create a user profile for all users created
@receiver(post_save, sender=User)
def Create_User_Profile(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)

# Signals used below to add users to each others friends list when a request has been accepted
@receiver(post_save, sender=Friendship)
def Add_Friend_To_List(sender, instance, created, **kwargs):
    request_sender = instance.sender
    request_receiver = instance.receiver
    if instance.status == 'Request Accepted':
        request_sender.friends.add(request_receiver.user)
        request_receiver.friends.add(request_sender.user)
        request_sender.save()
        request_sender.save()

# Signals used below to remove user from each others friends lists
@receiver(pre_delete, sender=Friendship)
def Remove_Friend_From_List(sender, instance, **kwargs):
    sender = instance.sender
    receiver = instance.receiver
    sender.friends.remove(receiver.user)
    receiver.friends.remove(sender.user)
    sender.save()
    receiver.save()