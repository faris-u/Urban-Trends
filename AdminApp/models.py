from django.db import models


# Create your models here.
class AdminModel(models.Model):
    admin_id = models.AutoField(primary_key=True)
    admin_name = models.CharField(max_length=200)
    admin_password = models.CharField(max_length=100)
    admin_email = models.EmailField()

    class Meta:
        db_table = 'admin_table'
