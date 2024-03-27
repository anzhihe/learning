本模块帮助在Django应用中集成百度Ueditor HTML编辑器,Django是Python世界最有影响力的web框架。
Ueditor HTML编辑器是百度开源的在线HTML编辑器,功能非常强大，像表格可以直接拖动调整单元格大小等。

本仓库是fork自：https://github.com/zhangfisher/DjangoUeditor
主要是因为发现原来的代码是基于python 2的语法，而我自己已经在用python 3.5了，有几个不兼容，所以想修改成python 3的语法
给用python 3的朋友们抛砖引玉一下


============
###[2015-10-05]     Version: 1.9.144

###* 语法的不同点，我自己试了一下，主要是下面两方面需要改动

##1. import
从同个文件夹下import，原代码是这样写的：import settings as USettings
但是在python 3中，应该写成：from . import settings as USettings
即from module import xxx
参考：[python 3文档](https://docs.python.org/3/tutorial/modules.html#intra-package-references)

##2. Exception
原代码这样写：

```python
    try:
        ...
    except Exception, E:
        print(E.message)
```

但在python 3中应该用as：

```python
    try:
        ...
    except Exception as E:
        print(E.message)
```

参考：[python3文档](https://docs.python.org/3/tutorial/errors.html#handling-exceptions)

##3. dict已经没有has_key属性了
原代码这样写：

```python
if self._upload_settings.has_key("filePathFormat"):
    uSettings['filePathFormat'] = calc_path(self._upload_settings['filePathFormat'], model_inst)
```

但在python 3中dict没有了has_key属性，所以应该换成get方法来判断：

```python
if self._upload_settings.get("filePathFormat", None):
    uSettings['filePathFormat'] = calc_path(self._upload_settings['filePathFormat'], model_inst)
```



---------------------------------------


使用方法
============
##1、安装方法

    * 将github整个源码包下载下来
        git clone https://github.com/cooljacket/DjangoUeditor
    * 然后，假设你的python安装目录是PYTHON_ROOT（我的是D:\soft\py3.5），直接复制DjangoUeditor文件夹到PYTHON_ROOT\Lib\site-packages\下就好了，比如我的就是D:\soft\py3.5\Lib\site-packages\
    * 之所以不使用原来的setup.py来安装，是因为我发现，用它的setup脚本会改动代码成原来的样子，也没去深究为什么，最后发现只需要直接复制过去就好了，而且卸载也很方便，直接删除就好了，没有什么依赖项和设置！
        
##2、在Django中安装DjangoUeditor
     在INSTALL_APPS里面增加DjangoUeditor app，如下：
        INSTALLED_APPS = (
            #........
            'DjangoUeditor',
        )
##3、配置urls
    url(r'^ueditor/',include('DjangoUeditor.urls' )),

##4、在models中的使用

    

```python
from DjangoUeditor.models import UEditorField
    class Blog(models.Model):
        Name=models.CharField(,max_length=100,blank=True)
        Content=UEditorField(u'内容   ',width=600, height=300, toolbars="full", imagePath="", filePath="", upload_settings={"imageMaxSize":1204000},
                 settings={},command=None,event_handler=myEventHander(),blank=True)
```

*说明*
    
 UEditorField继承自models.TextField,因此你可以直接将model里面定义的models.TextField直接改成UEditorField即可。
定义UEditorField时除了可以直接传入models.TextFieldUEditorField提供的参数外，还可以传入UEditorField提供的额外的参数
来控制UEditorField的外观、上传路径等。
UEditorField的参数如下：

* *width，height* :编辑器的宽度和高度，以像素为单位。
* *toolbars* :配置你想显示的工具栏，取值为mini,normal,full，代表小，一般，全部。如果默认的工具栏的按钮数量不符合您的要求，您可以在settings里面配置自己的显示按钮。参见后面介绍。
* *imagePath* :图片上传后保存的路径,如"images/",实现上传到"{{MEDIA_ROOT}}/images"文件夹。
    注意：如果imagePath值只设置文件夹，则未尾要有"/"
    imagePath可以按python字符串格式化：如"images/%(basename)s_%(datetime)s.%(extname)s"。这样如果上传test.png，则文件会
    被保存为"{{MEDIA_ROOT}}/images/test_20140625122399.png"。
    imagePath中可以使用的变量有：
    * time :上传时的时间，datetime.datetime.now().strftime("%H%M%S")
    * date ：上传时的日期，datetime.datetime.now().strftime("%Y%m%d")
    * datetime ：上传时的时间和日期，datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    * year : 年
    * month : 月
    * day : 日
    * rnd : 三位随机数，random.randrange(100,999)
    * basename ： 上传的文件名称，不包括扩展名
    * extname : 上传的文件扩展名
    * filename : 上传的文件名全称
* *filePath* : 附件上传后保存的路径，设置规则与imagePath一样。
* *upload_settings* : 字典值,
 例:upload_settings={
        imagePathFormat:"images/%(basename)s_%(datetime)s.%(extname)s",
        imageMaxSize:323232
        fileManagerListPath:"files"
   } 
     *  upload_settings的内容就是ueditor/php/config.json里面的配置内容，因此，你可以去看config.json或者官方文档内容来决定
            该如何配置upload_settings,基本上就是用来配置上传的路径、允许上传的文件扩展名、最大上传的文件大小之类的。
     *  上面的imagePath和filePath被单独提取出来配置，原因是因为这两个参数是最常使用到的，imagePath就相当于upload_settings里面的
                imagePathFormat，filePath就相当于upload_settings里面的filePathFormat。
     *  您upload_settings里面设置了imagePathFormat,也可以在UeditorField里面设置imagePath，效果是一样的。但是如果两者均设置，
   则imagePath优先级更高。
     *   涂鸦文件、截图、远程抓图、图片库的xxxxPathFormat如果没有配置，默认等于imagePath.
     *   远程文件库的xxxxPathFormat如果没有配置，默认等于filePath.
   
   
* *settings* : 字典值,配置项与ueditor/ueditor.config.js里面的配置项一致。
* *command* :  可以为Ueditor新增一个按钮、下拉框、对话框,例：

        Description = UEditorField(u'描述', blank=True, toolbars="full", imagePath="cool/", settings={"a": 1},
                               command=[myBtn(uiName="mybtn1", icon="d.png", title=u"1摸我", ajax_url="/ajaxcmd/"),
                                       myCombo(uiName="myCombo3",title=u"ccc",initValue="aaa")
                                        ])
        

以上代码可以会Ueditor增加一个按钮和一个下拉框。command是一个UEditorCommand的实例列表。如果你要在Ueditor的工具栏上增加一个
自定义按钮，方法如下：
        
        from DjangoUeditor.commands import UEditorButtonCommand,UEditorComboCommand
        #定义自己的按钮命令类
        class myBtn(UEditorButtonCommand):
            def onClick(self):
                return u"""
                    alert("爽!");       //这里可以写自己的js代码
                    editor.execCommand(uiName);
                """
            def onExecuteAjaxCommand(self,state):
            """  默认在command代码里面加入一段ajax代码，如果指定了ajax_url和重载本方法，则在单点按钮后
             会调用ajax_url.本方法重载是可选的。
             """
                if state=="success":
                    return u"""
                        alert("后面比较爽!"+xhr.responseText);//这里可以写ajax成功调用的js代码
                    """
                if state=="error":
                    return u"""
                        alert("讨厌，摸哪里去了！"+xhr.responseText);//这里可以写ajax错误调用的js代码
                    """
        
        UEditorButtonCommand有初始化参数:
                uiName:按钮名称
                title:按钮提示信息
                index:按钮显示的位置索引
                ajax_url：单击时调用的ajax url
                
        UEditorComboCommand可以在Ueditor上增加一个下拉框
        UEditorDialogCommand可以在Ueditor上增加一个对话框，一般与UEditorButtonCommand配合使用。暂未实现
        
* *event_handler* : 用来为Ueditor实例绑定事件侦听，比较当选择区改变时将按钮状态置为禁止。

        from DjangoUeditor.commands import UEditorEventHandler
        class myEventHander(UEditorEventHandler):
            def on_selectionchange(self):
                return """
                    function getButton(btnName){
                        var items=%(editor)s.ui.toolbars[0].items;
                        for(item in items){
                            if(items[item].name==btnName){
                                return items[item];
                            }
                        }
                    }
                    var btn=getButton("mybtn1");
                    var selRanage=id_Description.selection.getRange()
                    btn.setDisabled(selRanage.startOffset == selRanage.endOffset);
        
                """
        
        我们可以继承UEditorEventHandler创建自己的事件侦听类，例如上面myEventHander，然后在myEventHander中
        增加on_eventname的方法，在里面返回侦听该event的js代码。例如上例on_selectionchange,就会在前端js中
        生成id_Description.addListener('selectionchange', function () {.......});
        如果要侦听contentchange事件，就在myEventHander中增加一个on_contentchange方法，然后在该方法中返回js代码。
        

##5、在表单中使用非常简单，与常规的form字段没什么差别，如下：
    

```python
class TestUeditorModelForm(forms.ModelForm):
        class Meta:
            model=Blog
```
    ***********************************
    如果不是用ModelForm，可以有两种方法使用：

    1: 使用forms.UEditorField

    

```python
from  DjangoUeditor.forms import UEditorField
    class TestUEditorForm(forms.Form):
        Description=UEditorField("描述",initial="abc",width=600,height=800)
```
    
    2: widgets.UEditorWidget

    

```python
from  DjangoUeditor.widgets import UEditorWidget
    class TestUEditorForm(forms.Form):
        Content=forms.CharField(label="内容",widget=UEditorWidget(width=800,height=500, imagePath='aa', filePath='bb',toolbars={}))
```
    
    widgets.UEditorWidget和forms.UEditorField的输入参数与上述models.UEditorField一样。

    说明 关于第一种方法，需要在代码中建立相应的类（比如就在views.py中），并且需要在views.py渲染视图的时候返回到模板（template）中，对于上面的代码，具体使用可能如下（在views.py中）：

```python
    from DjangoUeditor.forms import UEditorField class TestUEditorForm(forms.Form):
        Description=UEditorField("描述",initial="abc",width=600,height=800)

    def edit_description_view(request):
        form = TestUEditorForm()
        return render(request,'edit-description.htm',{"form": form})
```

    而在edit-description.htm这个模板（template）里面，只需要在模板相应位置输出form即可：
```html
    <div class="edit-area"> 
        {{ form }} 
    </div>
```

##6、Settings配置
      在Django的Settings可以配置以下参数：
        

```
    UEDITOR_SETTINGS={
                "config":{
                   #这里放ueditor.config.js里面的配置项.......
                },
                "upload":{
                   #这里放php/config.json里面的配置项.......
                }
            }
```

##7、在模板里面：

```html
    <head>
        ......
        {{ form.media }}        #这一句会将所需要的CSS和JS加进来。
        ......
    </head>
```
    注：运行collectstatic命令，将所依赖的css,js之类的文件复制到{{STATIC_ROOT}}文件夹里面。

##8、高级运用：
     ****************
     动态指定imagePathFormat等文件路径
     ****************
     这几个路径文件用于保存上传的图片或附件，您可以直接指定路径，如：
          UEditorField('内容',imagePath="uploadimg/")
     则图片会被上传到"{{MEDIA_ROOT}}/uploadimg"文件夹，也可以指定为一个函数，如：

  

```python
    def getImagePath(model_instance=None):
          return "abc/"
```
      UEditorField('内容',imagePath=getImagePath)
      则图片会被上传到"{{MEDIA_ROOT}}/abc"文件夹。
     ****************
     使上传路径(如imagePathFormat)与Model实例字段值相关
     ****************
        在有些情况下，我们可能想让上传的文件路径是由当前Model实例字值组名而成，比如：
    

```python
    class Blog(Models.Model):
            Name=models.CharField('姓名',max_length=100,blank=True)
            Description=UEditorField('描述',blank=True,imagePath=getUploadPath,toolbars="full")
```

     id  |   Name    |       Description
     ------------------------------------
     1   |   Tom     |       ...........
     2   |   Jack    |       ...........

      我们想让第一条记录上传的图片或附件上传到"{{MEDIA_ROOT}}/Tom"文件夹,第2条记录则上传到"{{MEDIA_ROOT}}/Jack"文件夹。
      该怎么做呢，很简单。
  

```python
    def getUploadPath(model_instance=None):
          return "%s/" % model_instance.Name
```
      在Model里面这样定义：
      Description=UEditorField('描述',blank=True,imagePath=getUploadPath,toolbars="full")
      这上面model_instance就是当前model的实例对象。
      还需要这样定义表单对象：
  n

```python
    from  DjangoUeditor.forms import UEditorModelForm
      class UEditorTestModelForm(UEditorModelForm):
            class Meta:
                model=Blog
```
      特别注意：
         **表单对象必须是继承自UEditorModelForm，否则您会发现model_instance总会是None。
         **同时在Admin管理界面中，此特性无效，model_instance总会是None。
         **在新建表单中，model_instance由于还没有保存到数据库，所以如果访问model_instance.pk可能是空的。因为您需要在getUploadPath处理这种情况


##9、其他事项：

    **本程序版本号采用a.b.ccc,其中a.b是本程序的号，ccc是ueditor的版本号，如1.2.122，1.2是DjangoUeditor的版本号，122指Ueditor 1.2.2.
    **本程序安装包里面已经包括了Ueditor，不需要再额外安装。
    **目前暂时不支持ueditor的插件
    **别忘记了运行collectstatic命令，该命令可以将ueditor的所有文件复制到{{STATIC_ROOT}}文件夹里面
    **Django默认开启了CSRF中间件，因此如果你的表单没有加入{% csrf_token %}，那么当您上传文件和图片时会失败
   


