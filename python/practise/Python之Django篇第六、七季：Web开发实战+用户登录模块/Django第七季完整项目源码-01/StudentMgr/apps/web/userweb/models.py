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