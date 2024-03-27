# MxShop
慕课网生鲜电商项目源码-长期维护

**课程更新了django5分支，支持django5！**
	
	1. 拷贝git中对应django2分支中的xadmin源码
	
    2. model的ForeignKey 增加属性 on_delete=models.CASCADE(如果设置为models.SET_NULL 则该字段必须设置为null=True, blank=True
	3. 确保在settings中的installed_apps中第一行添加  'django.contrib.admin',
    4. 安装依赖包pip install requests
	