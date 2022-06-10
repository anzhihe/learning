from django.db import models

'''
id  name  parent
1   黑龙江  null
2   哈尔滨   1
3   xxx区   2

'''


# Create your models here.
class Area(models.Model):
    name = models.CharField(verbose_name='地区名字', max_length=100)
    parent = models.ForeignKey(to='self', blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


