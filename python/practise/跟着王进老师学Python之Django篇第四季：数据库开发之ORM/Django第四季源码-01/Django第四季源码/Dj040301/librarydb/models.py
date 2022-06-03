from django.db import models

# Create your models here.

"""
在数据库LibraryDB总有六张表：
Student ： 学生表  
Book： 图书表 
BorrowBook: 借书表 
Author: 作者表 
Press： 出版社表
BookType: 图书类别 
"""

# ==== Student : 学生表 =======
class Student(models.Model):
    sno = models.IntegerField('学号', null=False, primary_key=True)
    name = models.CharField('姓名', max_length=100, null=False, db_index=True)
    gender = models.CharField('性别', max_length=100, null=False)
    birthday = models.DateField('出生日期', null=False)
    mobile = models.CharField('手机号码', max_length=100, null=False, unique=True)
    email = models.CharField('邮箱地址', max_length=100, null=False, unique=True)
    address = models.CharField('家庭住址', max_length=200, null=False)

    def __str__(self):
        return "%s-%s-%s-%s-%s-%s-%s" % (self.sno, self.name, self.gender, self.birthday,
                                         self.mobile, self.email, self.address)
    class Meta:
        # 为当前类在数据库中生成的表命名，默认情况：App名称_类名字
        db_table = "Student"


# ==== BookType: 图书类别 ==========
class BookType(models.Model):
    name = models.CharField('类别名称', max_length=100, null=False)

    class Meta:
        db_table = 'BookType'

# ==== Press: 出版社 ===========
class Press(models.Model):
    name = models.CharField('出版社名称', max_length=100, null=False)
    city = models.CharField('所在城市', max_length=100, null=False)
    telno = models.CharField('联系电话', max_length=100, null=False)
    email = models.CharField('邮箱地址', max_length=100, null=False)
    address = models.CharField('地址', max_length=200, null=False)

    class Meta:
        db_table = 'Press'


# ==== Author:作者 ===========
class Author(models.Model):
    name = models.CharField('姓名', max_length=100, null=False)
    age = models.IntegerField('年龄',null=True)
    city = models.CharField('所在城市', max_length=100, null=False)
    telno = models.CharField('联系电话', max_length=100, null=False)
    email = models.CharField('邮箱地址', max_length=100, null=False)
    address = models.CharField('地址', max_length=200, null=False)

    class Meta:
        db_table = 'Author'

# ===== Book: 图书 ============
class Book(models.Model):
    bookid = models.IntegerField('图书编号', null=False, primary_key=True)
    bookname = models.CharField('图书名称',max_length=200, null=False, db_index=True)
    booktype = models.ForeignKey(to='BookType', on_delete=models.CASCADE)
    author = models.ForeignKey(to='Author', on_delete=models.CASCADE)
    press = models.ForeignKey(to='Press', on_delete=models.CASCADE)
    price = models.FloatField('价格', null=False)
    storagein = models.IntegerField('入库量', null=False)

    class Meta:
        db_table = 'Book'

# ====== BorrowBook:借书表 ==========
class BorrowBook(models.Model):
    sno = models.ForeignKey(to='Student', on_delete=models.CASCADE)
    bookid = models.ForeignKey(to='Book', on_delete=models.CASCADE)
    borrowdate = models.DateTimeField('借书时间')
    returndate = models.DateTimeField('归还时间')

    class Meta:
        db_table = 'BorrowBook'