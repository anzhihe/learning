# coding: utf-8

from django import forms
from widgets import UEditorWidget
from DjangoUeditor.models import UEditorField as ModelUEditorField


class UEditorField(forms.CharField):

    def __init__(
            self,
            label,
            width=600,
            height=300,
            toolbars="full",
            imagePath="",
            filePath="",
            upload_settings={},
            settings={},
            command=None,
            event_handler=None,
            *args,
            **kwargs):
        uSettings = locals().copy()
        del uSettings["self"], uSettings[
            "label"], uSettings["args"], uSettings["kwargs"]
        kwargs["widget"] = UEditorWidget(attrs=uSettings)
        kwargs["label"] = label
        super(UEditorField, self).__init__(*args, **kwargs)


# def UpdateUploadPath(model_form, model_inst=None):
#     """ 遍历model字段，如果是UEditorField则需要重新计算路径 """
#     if model_inst is not None:
#         try:
#             for field in model_inst._meta.fields:
#                 if isinstance(field, ModelUEditorField):
#                     model_form.__getitem__(
#                         field.name).field.widget.recalc_path(model_inst)
#         except:
#             pass
# 修改前
def UpdateUploadPath(model_form, model_inst=None):
    """ 遍历model字段，如果是UEditorField则需要重新计算路径 """
    if not model_inst:
        try:
            for field in model_inst._meta.fields:
                if isinstance(field, ModelUEditorField):
                    model_form.__getitem__(
                        field.name).field.widget.recalc_path(model_inst)
        except:
            pass


class UEditorModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(UEditorModelForm, self).__init__(*args, **kwargs)
        try:
            if "instance" in kwargs:
                UpdateUploadPath(self, kwargs["instance"])
            else:
                UpdateUploadPath(self, None)
        except Exception:
            pass
