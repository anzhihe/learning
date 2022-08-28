from django.db import models


# ==== 院系管理 ===
class Faculty(models.Model):
    name = models.CharField(verbose_name="院系名称", max_length=100, unique=True, null=False)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_Faculty"
        verbose_name = "Faculty"
        verbose_name_plural = "Faculty"

    def __str__(self):
        return '%s' % self.name


# ==== 专业管理 ===
class Major(models.Model):
    name = models.CharField(verbose_name="专业名称", max_length=100, unique=True, null=False)
    faculty = models.ForeignKey(verbose_name="所属院系", to=Faculty, on_delete=models.PROTECT)

    class Meta:
        managed = True
        app_label = "basicweb"
        db_table = "Basic_Major"
        verbose_name = "Major"
        verbose_name_plural = "Major"

    def __str__(self):
        return '%s' % self.name

