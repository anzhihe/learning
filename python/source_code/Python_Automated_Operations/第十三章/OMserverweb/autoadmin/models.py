# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.

from django.db import models

class ServerAppCateg(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    server_categ_id = models.IntegerField()
    app_categ_name = models.CharField(max_length=90)
    class Meta:
        db_table = u'server_app_categ'

class ServerFunCateg(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    server_categ_name = models.CharField(max_length=60)
    class Meta:
        db_table = u'server_fun_categ'

class ServerList(models.Model):
    server_name = models.CharField(max_length=39, primary_key=True)
    server_wip = models.CharField(max_length=45)
    server_lip = models.CharField(max_length=36)
    server_op = models.CharField(max_length=30)
    server_app_id = models.IntegerField()
    class Meta:
        db_table = u'server_list'

class ModuleList(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    module_name = models.CharField(max_length=60)
    module_caption = models.CharField(max_length=765)
    module_extend = models.CharField(max_length=6000)
    class Meta:
        db_table = u'module_list'
