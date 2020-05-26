from django.db import models

# Create your models here.
class Salvado(models.Model):
    nombre=models.CharField(
        max_length=100,
    )
    nacionalidad=models.CharField(
        max_length=100,
    )
    edad=models.CharField(
        max_length=100,
    )
    def __str__(self):
        return '{}'.format(self.nombre)
    def save(self):
        super(Salvado, self).save()

    class Meta:
        verbose_name_plural="Salvados"