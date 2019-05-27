from django.db import models

# Create your models here.
class ServerHistory(models.Model):
    id = models.IntegerField(primary_key=True, db_column='ID') # Field name made lowercase.
    history_id = models.IntegerField()
    history_ip = models.CharField(max_length=45)
    history_user = models.CharField(max_length=45)
    history_datetime = models.DateTimeField()
    db_datetime = models.DateTimeField()
    history_command = models.CharField(max_length=765)
    class Meta:
        db_table = u'server_history'