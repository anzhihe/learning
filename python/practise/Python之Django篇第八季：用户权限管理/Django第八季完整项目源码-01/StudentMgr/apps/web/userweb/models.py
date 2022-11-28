from django.db import models


# 用户登陆账号 --- Login
# 字段：loginid, loginpwd, name, status, department, position, mobile, email, last_login, create_time,edit_time
class Account(models.Model):
    loginid = models.CharField(verbose_name="登陆账号", max_length=20, primary_key=True, null=False, blank=False)
    loginpwd = models.CharField(verbose_name="密码", max_length=200, null=False, blank=False)
    name = models.CharField(verbose_name="姓名", max_length=50, null=False, blank=False)
    status = models.BooleanField(verbose_name="状态",null=False, blank=False, default=0)
    department = models.CharField(verbose_name="部门", max_length=50, blank=True, null=True,default=None)
    position = models.CharField(verbose_name="职位", max_length=50, null=True, blank=True,default=None)
    mobile = models.CharField(verbose_name="手机号码", max_length=50, null=True, blank=True,default=None)
    email = models.CharField(verbose_name="邮箱地址", max_length=100, null=True, blank=True, default=None)
    last_login = models.DateTimeField(verbose_name="上次登陆时间", null=True, blank=True, default=None)
    create_time = models.DateTimeField(verbose_name="创建时间", null=True, blank=True, default=None)
    edit_time = models.DateTimeField(verbose_name="修改时间", null=True, blank=True, default=None)

    class Meta:
        managed = True
        app_label = 'userweb'
        db_table = "user_Account"
        verbose_name = "Account"
        verbose_name_plural = "Account"

    def __str__(self):
        return "%s" % self.name


# 角色信息： Id,name, desc, account
class Roles(models.Model):
    id = models.AutoField(verbose_name="编号", primary_key=True, null=False, blank=False)
    name = models.CharField(verbose_name="名称", max_length=50, null=False, blank=False, unique=False)
    account = models.ManyToManyField(verbose_name="账号", to=Account, null=True)
    desc = models.CharField(verbose_name="描述", max_length=200, null=True, blank=True, default=None)

    class Meta:
        managed = True
        app_label = 'userweb'
        db_table = "user_Roles"
        verbose_name = "Roles"
        verbose_name_plural = "Roles"

    def __str__(self):
        return "%s" % self.name


# 顶级菜单：Menu [id, title, icon, order]
class Menu(models.Model):
    title = models.CharField(verbose_name="名称",max_length=100, null=False, blank=False, unique=True)
    icon = models.CharField(verbose_name="图标", max_length=100, null=True, blank=True, default=None)
    order = models.IntegerField(verbose_name="排序", null=True, blank=True, default=1)

    class Meta:
        managed = True
        app_label = 'userweb'
        db_table = "user_Menu"
        verbose_name = "Menu"
        verbose_name_plural = "Menu"

    def __str__(self):
        return "%s" % self.title


# 权限： Permission [id, title, url , roles, menu, order]
class Permission(models.Model):
    title = models.CharField(verbose_name="名称",max_length=100, null=False, blank=False)
    url = models.CharField(verbose_name="URL", max_length=200, null=True, blank=True, default=None)
    roles = models.ManyToManyField(verbose_name="角色", to=Roles, null=True, blank=True, default=None)
    menu = models.ForeignKey(verbose_name="菜单", to=Menu, on_delete=models.PROTECT, null=True)
    order = models.IntegerField(verbose_name="排序", unique=False, null=True, blank=True, default=1)

    class Meta:
        managed = True
        app_label = 'userweb'
        db_table = "user_Permission"
        verbose_name = "Permission"
        verbose_name_plural = "Permission"

    def __str__(self):
        return "%s" % self.title