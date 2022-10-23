from django.db import models

# Create your models here.
class user(models.Model):
     user_id = models.IntegerField(primary_key=True)
     user_name = models.CharField(max_length=50)
     user_pass = models.IntegerField()
     user_email = models.IntegerField()
