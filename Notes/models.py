from django.db import models
from User.models import user


class notes(models.Model):
    note_id = models.IntegerField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

