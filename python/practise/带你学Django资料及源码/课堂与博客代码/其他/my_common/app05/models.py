from django.db import models


# Create your models here.
class GunType(models.Model):
    name = models.CharField(verbose_name='类型', max_length=10)
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '种类'
        verbose_name_plural = verbose_name


class Gun(models.Model):
    name = models.CharField(verbose_name='名字', max_length=20)
    num = models.IntegerField(verbose_name='子弹数量')
    created_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)

    gt = models.ForeignKey(to=GunType, verbose_name='属于种类', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '枪'
        verbose_name_plural = verbose_name

    # 自定义函数
    def show_num(self):
        return str(self.num) + "发"

    show_num.short_description = '子弹数量'
