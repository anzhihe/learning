from django.db import models

# Create your models here.


# 创建类 --- > 对应数据库中表
# Student ---> 字段（SNO:int, name:varchar,gender:varchar, birthday:date,
#                    mobile:str, email:str, address:str）
class Student(models.Model):
    sno = models.IntegerField(null=False, primary_key=True) # 学号，主键！
    name = models.CharField(max_length=100, null=False) # 姓名
    gender = models.CharField(max_length=100, null=False) # 性别
    birthday = models.DateField(null=False) # 出生日期
    mobile = models.CharField(max_length=100,null=False)  # 手机号码
    email = models.CharField(max_length=100, null=False)  # 邮箱地址
    address = models.CharField(max_length=100, null=False)  # 家庭住址

    def __str__(self):
        return "学号：%s-姓名：%s-性别：%s-出生日期：%s-手机号码：%s-邮箱地址：%s-家庭住址：%s" %(self.sno, self.name, self.gender, self.birthday,
                                        self.mobile, self.email, self.address)



class Table01(models.Model):
    sno = models.AutoField('学号', null=False, primary_key=True, help_text='学号')
    number = models.IntegerField(null=False)
    name = models.CharField(max_length=200, null=False)
    date01 = models.DateField(null=False)  # Datetime.date() --- 日期
    date02 = models.DateTimeField(null=False) # Datetime.datetime() --- 日期时间
    money = models.FloatField(null=False)  # 映射为Float
    IsReady = models.BooleanField(null=False)  # 映射为tinyint
    desc = models.TextField(null=True, unique=False) # 对应mysql中的longtext

class Table02(models.Model):
    sno = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=200, null=False, db_index=True)
    gender = models.CharField(max_length=100, null=False, default='女')
    mobile = models.CharField(max_length=100, null=False, unique=True)
    email = models.CharField(max_length=100, null=False, unique=True)
    create_date = models.DateTimeField(auto_now_add=True)   # 默认插入数据的时候记录时间
    update_date = models.DateTimeField(auto_now=True)   #  默认记录修改的时间


# 在ORM中必须每个类中必须有一个主键，如果没有创建，系统自动添加一个
# id = models.AutoField(null=False, primary_key=True)
class Classes(models.Model): # --- 记录了班级 ----
    class_id = models.IntegerField(null=False, primary_key=True)
    class_name = models.CharField(max_length=100, null=False, db_index=True)

class Studentes(models.Model): # ---- 记录了学生 ---
    sno = models.IntegerField(null=False, primary_key=True)
    name = models.CharField(max_length=100, null=False, db_index=True)
    # --- 创建外键 --> 关联班级
    stu_class = models.ForeignKey(to='Classes', on_delete=models.CASCADE)






