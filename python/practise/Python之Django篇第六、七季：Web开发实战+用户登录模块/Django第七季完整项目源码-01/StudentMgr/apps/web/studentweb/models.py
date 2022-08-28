from django.db import models
from basicweb.models import Faculty, Major


# === 学生的类 ====
class Student(models.Model):
    sno = models.CharField(verbose_name="学号", primary_key=True, max_length=100)
    name = models.CharField(verbose_name='姓名', max_length=100)
    gender = models.CharField(verbose_name='性别', max_length=100, choices=(('男', '男'), ('女', '女')))
    birthday = models.DateField(verbose_name='出生日期')
    mobile = models.CharField(verbose_name='手机号码', max_length=100)
    email = models.EmailField(verbose_name='邮箱地址', max_length=100)
    address = models.CharField(verbose_name='手机号码', max_length=250)
    faculty = models.ForeignKey(verbose_name='院系名称', to=Faculty, on_delete=models.PROTECT)
    major = models.ForeignKey(verbose_name='所学专业', to=Major, on_delete=models.PROTECT)
    start_date = models.DateField(verbose_name='入学时间')
    status = models.CharField(verbose_name='状态', max_length=100, choices=(
        ('在校', '在校'), ('毕业', '毕业'), ('休学', '休学'), ('开除', '开除')), default='在校')

    class Meta:
        managed = True
        app_label = 'studentweb'
        db_table = "Stu_Student"
        verbose_name = "Student"
        verbose_name_plural = "Student"

    def __str__(self):
        return "%s" % self.name


# === 学生照片 ====
# 字段：id(自动编号), name(日期+ 4位随机值.后缀), remark, create_time
class StudentImage(models.Model):
    name = models.CharField(verbose_name="图片名称", max_length=50, null=False, blank=False)
    remark = models.CharField(verbose_name="标注", max_length=250, null=True, blank=True)
    create_time = models.DateTimeField(verbose_name="上传时间")

    class Meta:
        managed = True
        app_label = 'studentweb'
        db_table = "Stu_StudentImage"
        verbose_name = "StudentImage"
        verbose_name_plural = "StudentImage"

    def __str__(self):
        return "%s" % self.name