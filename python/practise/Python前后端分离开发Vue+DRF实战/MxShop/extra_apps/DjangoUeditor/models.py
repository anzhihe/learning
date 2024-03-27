# coding: utf-8
from django.db import models
from django.contrib.admin import widgets as admin_widgets
from .widgets import UEditorWidget, AdminUEditorWidget


class UEditorField(models.TextField):
    """
    百度HTML编辑器字段,初始化时，可以提供以下参数
        initial:初始内容
        toolbars:提供工具按钮列表,取值为列表，如['bold', 'italic'],取值为：mini,normal,full，代表小，一般，全部
        imagePath:图片上传的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹
        filePath:附件上传的路径,如"files/",实现上传到"{{MEDIA_ROOT}}/files"文件夹
    """

    def __init__(
            self,
            verbose_name=None,
            width=600,
            height=300,
            toolbars="full",
            imagePath="",
            filePath="",
            upload_settings={},
            settings={},
            command=None,
            event_handler=None,
            **kwargs):
        self.ueditor_settings = locals().copy()
        kwargs["verbose_name"] = verbose_name
        del self.ueditor_settings["self"], self.ueditor_settings[
            "kwargs"], self.ueditor_settings["verbose_name"]
        super(UEditorField, self).__init__(**kwargs)

    def formfield(self, **kwargs):
        defaults = {'widget': UEditorWidget(attrs=self.ueditor_settings)}
        defaults.update(kwargs)
        if defaults['widget'] == admin_widgets.AdminTextareaWidget:
            defaults['widget'] = AdminUEditorWidget(
                attrs=self.ueditor_settings)
        return super(UEditorField, self).formfield(**defaults)

# 以下支持south
try:
    from south.modelsinspector import add_introspection_rules
    add_introspection_rules([], ["^DjangoUeditor\.models\.UEditorField"])
except:
    pass
