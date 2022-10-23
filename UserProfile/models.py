from django.db import models
from user.models import user

class UserProfile(models.Model):
    p_id = models.IntegerField(primary_key=True)

    ph_no = models.IntegerField()
    user = models.ForeignKey(user, on_delete=models.CASCADE)
    notes = models.CharField(max_length=80)



