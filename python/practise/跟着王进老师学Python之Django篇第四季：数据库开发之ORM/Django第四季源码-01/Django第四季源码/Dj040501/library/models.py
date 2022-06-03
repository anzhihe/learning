# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    authorid = models.IntegerField(db_column='AuthorID', primary_key=True,  null=False, verbose_name='编号')  # Field name made lowercase.
    authorname = models.CharField(db_column='AuthorName', max_length=255, null=False, verbose_name='姓名')  # Field name made lowercase.
    authorage = models.IntegerField(db_column='AuthorAge', blank=True, null=True, verbose_name='年龄')  # Field name made lowercase.
    authorcity = models.CharField(db_column='AuthorCity', max_length=255, blank=True, null=True, verbose_name='所在城市')  # Field name made lowercase.
    authortelno = models.CharField(db_column='AuthorTelNo', max_length=255, blank=True, null=True, verbose_name='联系电话')  # Field name made lowercase.
    authoremail = models.CharField(db_column='AuthorEMail', max_length=255, blank=True, null=True, verbose_name='邮箱')  # Field name made lowercase.
    authorworkaddress = models.CharField(db_column='AuthorWorkAddress', max_length=255, blank=True, null=True, verbose_name='地址')  # Field name made lowercase.

    def __str__(self):
        return "%d-%s"%(self.authorid, self.authorname)

    class Meta:
        managed = True
        db_table = 'Author'
        ordering = ['authorid']
        verbose_name = '作者'
        verbose_name_plural = '作者'

class Booktype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, null=False, verbose_name='编号')  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=255,  null=False, verbose_name='类别名称')  # Field name made lowercase.

    def __str__(self):
        return self.typename

    class Meta:
        managed = True
        db_table = 'BookType'
        ordering = ['id']
        verbose_name = '图书类别'
        verbose_name_plural = '图书类别'

class Press(models.Model):
    pressid = models.IntegerField(db_column='PressID',primary_key=True, null=False, verbose_name='编号')  # Field name made lowercase.
    pressname = models.CharField(db_column='PressName', max_length=255, null=False, verbose_name='出版社名称')  # Field name made lowercase.
    presscity = models.CharField(db_column='PressCity', max_length=255, blank=True, null=True, verbose_name='所在城市')  # Field name made lowercase.
    presstelno = models.CharField(db_column='PressTelNO', max_length=255, blank=True, null=True, verbose_name='联系电话')  # Field name made lowercase.
    pressemail = models.CharField(db_column='PressEmail', max_length=255, blank=True, null=True, verbose_name='邮箱')  # Field name made lowercase.
    pressaddress = models.CharField(db_column='PressAddress', max_length=255, blank=True, null=True, verbose_name='地址')  # Field name made lowercase.

    def __str__(self):
        return "%d-%s"%(self.pressid, self.pressname)

    class Meta:
        managed = True
        db_table = 'Press'
        ordering = ['pressid']
        verbose_name = '出版社'
        verbose_name_plural = '出版社'

class Book(models.Model):
    bookid = models.IntegerField(db_column='BookID', null=False, primary_key=True, verbose_name='图书编号')  # Field name made lowercase.
    bookname = models.CharField(db_column='BookName', max_length=255, blank=True, null=True, verbose_name='图书名称')  # Field name made lowercase.
    booktype = models.ForeignKey('Booktype', models.DO_NOTHING, db_column='BookTypeID', verbose_name='图书类别')
    bookauthor = models.ForeignKey('Author', models.DO_NOTHING, db_column='BookAuthorID', verbose_name='图书作者')
    bookprice = models.FloatField(db_column='BookPrice', blank=True, null=True, verbose_name='图书价格')  # Field name made lowercase.
    bookpress = models.ForeignKey('Press', models.DO_NOTHING, db_column='BookPressID', verbose_name='出版社')
    booksumno = models.IntegerField(db_column='BookSumNo', blank=True, null=True, verbose_name='库存量')  # Field name made lowercase.

    def __str__(self):
        return "%d-%s"%(self.bookid, self.bookname)

    class Meta:
        managed = True
        db_table = 'Book'
        ordering = ['bookid']
        verbose_name = '图书'
        verbose_name_plural = '图书'

class Student(models.Model):
    sno = models.IntegerField(db_column='SNO', null=False, primary_key=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=255, null=False)  # Field name made lowercase.
    sage = models.IntegerField(db_column='Age', blank=True, null=False)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=False)  # Field name made lowercase.
    mobileno = models.CharField(db_column='Mobile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stuemail = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return "%d-%s"%(self.sno, self.sname)

    class Meta:
        managed = True
        db_table = 'Student'
        ordering = ['sno']
        verbose_name = '学生'
        verbose_name_plural = '学生'

class Borrowbook(models.Model):
    id = models.IntegerField(db_column='ID', null=False, primary_key=True)  # Field name made lowercase.
    sno = models.ForeignKey('Student', models.DO_NOTHING, db_column='SNO')
    bookid = models.ForeignKey('Book', models.DO_NOTHING, db_column='BookId')
    borrowdate = models.DateTimeField(db_column='BorrowDate', blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateTimeField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.
    def __str__(self):
        return self.id

    class Meta:
        managed = True
        db_table = 'BorrowBook'
        ordering = ['id']
        verbose_name = '借书'
        verbose_name_plural = '借书'


