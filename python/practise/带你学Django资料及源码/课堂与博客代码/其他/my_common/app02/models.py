from django.db import models


# Create your models here.

class Cat(models.Model):
    name = models.CharField(verbose_name='猫', max_length=15)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '猫'
        verbose_name_plural = verbose_name
