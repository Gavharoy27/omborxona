from django.core.validators import MinValueValidator
from django.db import models
from main.models import Mahsulot, Bolim, Mijoz


class Sotuv(models.Model):
    mahsulot = models.ForeignKey(Mahsulot, on_delete=models.CASCADE)
    mijoz = models.ForeignKey(Mijoz, on_delete=models.CASCADE)
    miqdor = models.FloatField(validators=[MinValueValidator(0.0)])
    sana = models.DateTimeField(auto_now_add=True)
    jami_summa = models.FloatField(validators=[MinValueValidator(0.0)])
    tolandi = models.FloatField(validators=[MinValueValidator(0.0)])
    qarz = models.FloatField(validators=[MinValueValidator(0.0)])
    bolim = models.ForeignKey(Bolim, on_delete=models.CASCADE)

    def __str__(self):
        return f"{{self.mahsulot}}-{{self.mijoz}}"