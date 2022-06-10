# coding:utf-8
from django import forms
from django.conf import settings
from django.contrib.admin.widgets import AdminTextareaWidget
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from django.utils.http import urlencode
from . import settings as USettings
from  .commands import *

# 修正输入的文件路径,输入路径的标准格式：abc,不需要前后置的路径符号
#如果输入的路径参数是一个函数则执行，否则可以拉接受时间格式化，用来生成如file20121208.bmp的重命名格式
def calc_path(OutputPath, instance=None):
    if callable(OutputPath):
        try:
            OutputPath = OutputPath(instance)
        except:
            OutputPath = ""
    else:
        try:
            import datetime
            OutputPath = datetime.datetime.now().strftime(OutputPath)
        except:
            pass

    return OutputPath


class UEditorWidget(forms.Textarea):
    def __init__(self,attrs=None):

        params=attrs.copy()

        width=params.pop("width")
        height=params.pop("height")
        toolbars=params.pop("toolbars","full")
        imagePath=params.pop("imagePath","")
        filePath=params.pop("filePath","")
        upload_settings=params.pop("upload_settings",{})
        settings=params.pop("settings",{})
        command=params.pop("command",None)
        event_handler=params.pop("event_handler",None)

        #扩展命令
        self.command=command
        self.event_handler=event_handler
        #上传路径
        self.upload_settings = upload_settings.copy()
        self.upload_settings.update({
            "imagePathFormat": imagePath,
            "filePathFormat": filePath
        })
        #保存
        self._upload_settings =self.upload_settings.copy()
        self.recalc_path(None)

        self.ueditor_settings ={
            'toolbars':toolbars,
            'initialFrameWidth':width,
            'initialFrameHeight':height
        }
        #以下处理工具栏设置，将normal,mini等模式名称转化为工具栏配置值
        try:
            if type(toolbars)==str:
                if toolbars =="full":
                    del self.ueditor_settings['toolbars']
                else:
                    self.ueditor_settings["toolbars"]=USettings.TOOLBARS_SETTINGS[toolbars]
        except:
            pass
        self.ueditor_settings.update(settings)
        super(UEditorWidget, self).__init__(attrs)

    def recalc_path(self, model_inst):
        """计算上传路径,允许是function"""
        try:
            uSettings = self.upload_settings
            if self._upload_settings.get("filePathFormat"):
                uSettings['filePathFormat'] = calc_path(self._upload_settings['filePathFormat'], model_inst)
            if self._upload_settings.get("imagePathFormat"):
                uSettings['imagePathFormat'] = calc_path(self._upload_settings['imagePathFormat'], model_inst)
            if self._upload_settings.get("scrawlPathFormat"):
                uSettings['scrawlPathFormat'] = calc_path(self._upload_settings['scrawlPathFormat'], model_inst)
            if self._upload_settings.get("videoPathFormat"):
                uSettings['videoPathFormat'] = calc_path(self._upload_settings['videoPathFormat'], model_inst),
            if self._upload_settings.get("snapscreenPathFormat"):
                uSettings['snapscreenPathFormat'] = calc_path(self._upload_settings['snapscreenPathFormat'], model_inst)
            if self._upload_settings.get("catcherPathFormat"):
                uSettings['catcherPathFormat'] = calc_path(self._upload_settings['catcherPathFormat'], model_inst)
            if self._upload_settings.get("imageManagerListPath"):
                uSettings['imageManagerListPath'] = calc_path(self._upload_settings['imageManagerListPath'], model_inst)
            if self._upload_settings.get("fileManagerListPath"):
                uSettings['fileManagerListPath'] = calc_path(self._upload_settings['fileManagerListPath'], model_inst)
            #设置默认值，未指定涂鸦、截图、远程抓图、图片目录时,默认均等于imagePath
            if uSettings['imagePathFormat']!="":
                uSettings['scrawlPathFormat']=uSettings['scrawlPathFormat'] if self._upload_settings.get("scrawlPathFormat") else uSettings['imagePathFormat']
                uSettings['videoPathFormat']=uSettings['videoPathFormat'] if self._upload_settings.get("videoPathFormat") else uSettings['imagePathFormat']
                uSettings['snapscreenPathFormat']=uSettings['snapscreenPathFormat'] if self._upload_settings.get("snapscreenPathFormat") else uSettings['imagePathFormat']
                uSettings['catcherPathFormat']=uSettings['catcherPathFormat'] if self._upload_settings.get("catcherPathFormat") else uSettings['imagePathFormat']
                uSettings['imageManagerListPath']=uSettings['imageManagerListPath'] if self._upload_settings.get("imageManagerListPath") else uSettings['imagePathFormat']
            if uSettings['filePathFormat']!="":
                uSettings['fileManagerListPath']=uSettings['fileManagerListPath'] if self._upload_settings.get("fileManagerListPath") else uSettings['filePathFormat']
        except:
            pass


    def render(self, name, value, attrs=None):
        if value is None: value = ''
        #传入模板的参数
        editor_id="id_%s" % name.replace("-", "_")
        uSettings={
            "name": name,
            "id": editor_id,
            "value":value
        }
        if isinstance(self.command,list):
            cmdjs=""
            if isinstance(self.command,list):
                for cmd in self.command:
                    cmdjs=cmdjs+cmd.render(editor_id)
            else:
                cmdis=self.command.render(editor_id)
            uSettings["commands"]=cmdjs


        uSettings["settings"] = self.ueditor_settings.copy()
        uSettings["settings"].update({
            "serverUrl": "/ueditor/controller/?%s" % urlencode(self._upload_settings)
        })
        #生成事件侦听
        if self.event_handler:
            uSettings["bindEvents"]=self.event_handler.render(editor_id)

        context = {
            'UEditor': uSettings,
            'STATIC_URL': settings.STATIC_URL,
            'STATIC_ROOT': settings.STATIC_ROOT,
            'MEDIA_URL': settings.MEDIA_URL,
            'MEDIA_ROOT': settings.MEDIA_ROOT
        }
        return mark_safe(render_to_string('ueditor.html', context))

    class Media:
        js = ("ueditor/ueditor.config.js",
              "ueditor/ueditor.all.min.js")


class AdminUEditorWidget(AdminTextareaWidget,UEditorWidget ):
    def __init__(self, **kwargs):
        super(AdminUEditorWidget, self).__init__(**kwargs)
