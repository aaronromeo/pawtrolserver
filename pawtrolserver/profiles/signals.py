import uuid

from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils import timezone

# from profiles.models import PawtrolUser


# @receiver(pre_save, sender=PawtrolUser)
# @receiver(pre_save, sender=User)
# def generate_username(sender, instance, **kwargs):
#     if not instance.id and not instance.username:
#         while True:
#             proposed_username = str(uuid.uuid4())[:30]
#             try:
#                 User.objects.get(username=proposed_username)
#             except User.DoesNotExist:
#                 instance.username = proposed_username
#                 break
