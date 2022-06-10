from django.db import models


# Create your models here.


# 英雄类型表
class HeroType(models.Model):
    title = models.CharField(verbose_name='名称', max_length=5)

    def __str__(self):
        return self.title


# 英雄
class Hero(models.Model):
    name = models.CharField(verbose_name='名字', max_length=10)
    gender = models.IntegerField(verbose_name='性别')
    age = models.IntegerField(verbose_name='年龄')
    ht = models.ForeignKey(to=HeroType, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


# 技能表
class Kill(models.Model):
    name = models.CharField(verbose_name='技能名字', max_length=10)
    cd = models.IntegerField(verbose_name='冷却时间')
    da = models.IntegerField(verbose_name='伤害值')
    hero = models.ForeignKey(to=Hero, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
