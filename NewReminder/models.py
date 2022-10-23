from django.db import models

# Create your models here.
class newreminder(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=40)
    date = models.IntegerField()
    time = models.IntegerField()
    repeat = models.CharField(max_length=50)
    notes = models.CharField(max_length=60)

