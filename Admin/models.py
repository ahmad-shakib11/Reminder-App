from django.db import models

# Create your models here.
class home(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.IntegerField()
    username = models.CharField(max_length=40)
