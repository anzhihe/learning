# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Adminmodules(models.Model):
    moduleid = models.AutoField(db_column='ModuleId', primary_key=True)  # Field name made lowercase.
    modulename = models.CharField(db_column='ModuleName', max_length=100)  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=100)  # Field name made lowercase.
    icon = models.CharField(db_column='ICON', max_length=100)  # Field name made lowercase.
    priority = models.IntegerField(db_column='Priority', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True    # 可管理 --- 这个类和后台表关联
        db_table = 'AdminModules'


class Login(models.Model):
    loginid = models.CharField(db_column='LoginId', primary_key=True, max_length=20)  # Field name made lowercase.
    loginpwd = models.CharField(db_column='LoginPwd', max_length=20)  # Field name made lowercase.
    username = models.CharField(db_column='UserName', max_length=20)  # Field name made lowercase.
    isenable = models.IntegerField(db_column='IsEnable')  # Field name made lowercase.
    positionid = models.ForeignKey('Position', models.DO_NOTHING, db_column='PositionId')  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='CreateTime', blank=True, null=True)  # Field name made lowercase.
    lastlogintime = models.DateTimeField(db_column='LastLoginTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Login'


class Position(models.Model):
    positionid = models.AutoField(db_column='PositionId', primary_key=True)  # Field name made lowercase.
    positionname = models.CharField(db_column='PositionName', max_length=20)  # Field name made lowercase.
    description = models.CharField(db_column='Description', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Position'


class Product(models.Model):
    productid = models.CharField(db_column='ProductId', primary_key=True, max_length=20)  # Field name made lowercase.
    barcode = models.CharField(db_column='BarCode', unique=True, max_length=20)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase.
    categoryid = models.ForeignKey('Productcategory', models.DO_NOTHING, db_column='CategoryId', blank=True, null=True)  # Field name made lowercase.
    inventory = models.IntegerField(db_column='Inventory')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'Product'


class Productcategory(models.Model):
    categoryid = models.AutoField(db_column='CategoryId', primary_key=True)  # Field name made lowercase.
    categoryname = models.CharField(db_column='CategoryName', max_length=100)  # Field name made lowercase.
    decription = models.CharField(db_column='Decription', max_length=200, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'ProductCategory'


class Saleslist(models.Model):
    serialnumber = models.CharField(db_column='SerialNumber', primary_key=True, max_length=20)  # Field name made lowercase.
    totalnumber = models.IntegerField(db_column='TotalNumber')  # Field name made lowercase.
    totalprice = models.FloatField(db_column='TotalPrice')  # Field name made lowercase.
    receivemoney = models.FloatField(db_column='ReceiveMoney')  # Field name made lowercase.
    returnmoney = models.FloatField(db_column='ReturnMoney')  # Field name made lowercase.
    loginid = models.ForeignKey(Login, models.DO_NOTHING, db_column='LoginId', blank=True, null=True)  # Field name made lowercase.
    buytime = models.DateTimeField(db_column='BuyTime', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SalesList'


class Saleslistdetail(models.Model):
    detailid = models.AutoField(db_column='DetailId', primary_key=True)  # Field name made lowercase.
    serialnumber = models.ForeignKey(Saleslist, models.DO_NOTHING, db_column='SerialNumber', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey(Product, models.DO_NOTHING, db_column='ProductId', blank=True, null=True)  # Field name made lowercase.
    productname = models.CharField(db_column='ProductName', max_length=200)  # Field name made lowercase.
    unit = models.CharField(db_column='Unit', max_length=20)  # Field name made lowercase.
    unitprice = models.FloatField(db_column='UnitPrice')  # Field name made lowercase.
    number = models.IntegerField(db_column='Number')  # Field name made lowercase.
    money = models.FloatField(db_column='Money')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'SalesListDetail'
