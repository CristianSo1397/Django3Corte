from django.db import models

# Create your models here.
class Aliado(models.Model):
    nombre=models.CharField(
        max_length=100,
    )
    poder=models.CharField(
        max_length=100,
    )
    mundo=models.CharField(
        max_length=100,
    )
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        super(Aliado, self).save()

    class Meta:
        verbose_name_plural="Aliados"