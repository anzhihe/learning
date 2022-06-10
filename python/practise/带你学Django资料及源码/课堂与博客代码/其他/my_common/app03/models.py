from django.db import models
from DjangoUeditor.models import UEditorField


# Create your models here.
class News(models.Model):
    title = models.CharField(verbose_name='标题', max_length=100)
    content = UEditorField(width=600, height=300, toolbars="full",
                           imagePath="news/%(basename)s_%(datetime)s.%(extname)s", filePath="files/")

    def __str__(self): return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
