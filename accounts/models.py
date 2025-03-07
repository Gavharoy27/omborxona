from django.db import models
from main.models import *

class Sotuvchi(models.Model):
    rasm = models.ImageField(upload_to='sotuvchilar/', null=True, blank=True)
    bolim = models.ForeignKey(Bolim, on_delete=models.SET_NULL, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.user.username

