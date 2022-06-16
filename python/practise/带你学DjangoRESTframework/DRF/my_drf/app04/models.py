from django.db import models


# Create your models here.
class Game(models.Model):
    name = models.CharField(verbose_name='游戏名字', max_length=10)
    desc = models.CharField(verbose_name='描述', max_length=20)
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
