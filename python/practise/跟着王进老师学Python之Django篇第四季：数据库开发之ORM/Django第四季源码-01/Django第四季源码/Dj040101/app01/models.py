from django.db import models

# Create your models here.


# 定义Student类
class Student(models.Model):   # --- 关联 --- Student
    sno = models.IntegerField("学号", null=False, primary_key=True)
    name = models.CharField("姓名", max_length=100, null=False)
    gender = models.CharField("性别", max_length=100, null=False)
    birthday = models.DateField("出生日期", null=False)
    mobile = models.CharField("手机号码", max_length=100)
    email = models.CharField("邮箱地址", max_length=100)
    address = models.CharField("家庭住址", max_length=200)

    def __str__(self):
        return "%s-%s-%s-%s-%s-%s-%s" %(self.sno, self.name, self.gender, self.birthday,
                                        self.mobile, self.email, self.address)