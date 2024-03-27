# -*- coding: utf-8 -*-
__author__ = 'bobby'
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
from django.contrib.auth import get_user_model


from user_operation.models import UserFav


@receiver(post_save, sender=UserFav)
def create_userfav(sender, instance=None, created=False, **kwargs):
    if created:
        goods = instance.goods
        goods.fav_num += 1
        goods.save()


@receiver(post_delete, sender=UserFav)
def delete_userfav(sender, instance=None, created=False, **kwargs):
    goods = instance.goods
    goods.fav_num -= 1
    goods.save()
