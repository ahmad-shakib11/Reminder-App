from django.db import models
from django.contrib.auth.models import User


class notes(models.Model):
    note_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING,default=None,null=True)

