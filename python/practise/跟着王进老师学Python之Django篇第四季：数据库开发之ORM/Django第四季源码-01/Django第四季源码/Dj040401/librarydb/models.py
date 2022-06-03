# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Author(models.Model):
    authorid = models.IntegerField(db_column='AuthorID', primary_key=True,  null=False)  # Field name made lowercase.
    authorname = models.CharField(db_column='AuthorName', max_length=255, null=False)  # Field name made lowercase.
    authorage = models.IntegerField(db_column='AuthorAge', blank=True, null=True)  # Field name made lowercase.
    authorcity = models.CharField(db_column='AuthorCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authortelno = models.CharField(db_column='AuthorTelNo', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authoremail = models.CharField(db_column='AuthorEMail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    authorworkaddress = models.CharField(db_column='AuthorWorkAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Author'

class Booktype(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True, null=False)  # Field name made lowercase.
    typename = models.CharField(db_column='TypeName', max_length=255,  null=False)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BookType'

class Press(models.Model):
    pressid = models.IntegerField(db_column='PressID',primary_key=True, null=False)  # Field name made lowercase.
    pressname = models.CharField(db_column='PressName', max_length=255, null=False)  # Field name made lowercase.
    presscity = models.CharField(db_column='PressCity', max_length=255, blank=True, null=True)  # Field name made lowercase.
    presstelno = models.CharField(db_column='PressTelNO', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pressemail = models.CharField(db_column='PressEmail', max_length=255, blank=True, null=True)  # Field name made lowercase.
    pressaddress = models.CharField(db_column='PressAddress', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Press'

class Book(models.Model):
    bookid = models.IntegerField(db_column='BookID', null=False, primary_key=True)  # Field name made lowercase.
    bookname = models.CharField(db_column='BookName', max_length=255, blank=True, null=True)  # Field name made lowercase.
    booktype = models.ForeignKey('Booktype', models.DO_NOTHING, db_column='BookTypeID')
    bookauthor = models.ForeignKey('Author', models.DO_NOTHING, db_column='BookAuthorID')
    bookprice = models.FloatField(db_column='BookPrice', blank=True, null=True)  # Field name made lowercase.
    bookpress = models.ForeignKey('Press', models.DO_NOTHING, db_column='BookPressID')
    booksumno = models.IntegerField(db_column='BookSumNo', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Book'

class Student(models.Model):
    sno = models.IntegerField(db_column='SNO', null=False, primary_key=True)  # Field name made lowercase.
    sname = models.CharField(db_column='SName', max_length=255, null=False)  # Field name made lowercase.
    sage = models.IntegerField(db_column='Age', blank=True, null=False)  # Field name made lowercase.
    gender = models.CharField(db_column='Gender', max_length=255, blank=True, null=False)  # Field name made lowercase.
    mobileno = models.CharField(db_column='Mobile', max_length=255, blank=True, null=True)  # Field name made lowercase.
    stuemail = models.CharField(db_column='Email', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Student'

class Borrowbook(models.Model):
    id = models.IntegerField(db_column='ID', null=False, primary_key=True)  # Field name made lowercase.
    sno = models.ForeignKey('Student', models.DO_NOTHING, db_column='SNO')
    bookid = models.ForeignKey('Book', models.DO_NOTHING, db_column='BookId')
    borrowdate = models.DateTimeField(db_column='BorrowDate', blank=True, null=True)  # Field name made lowercase.
    returndate = models.DateTimeField(db_column='ReturnDate', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'BorrowBook'


