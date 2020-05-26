from django.db import models

# Create your models here.
class Patrocinador(models.Model):
    nombre = models.CharField(
        max_length=100,
    )
    fondos =models.IntegerField()
    def __str__(self):
        return '{}'.format(self.nombre)

    def save(self):
        super(Patrocinador, self).save()
    
    class Meta:
        verbose_name_plural="Patrocinadores"