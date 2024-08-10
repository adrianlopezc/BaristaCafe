from django.db import models

class Menu(models.Model):
    title           = models.CharField(max_length=100, verbose_name='Título')
    description     = models.CharField(max_length=100, verbose_name='Descripción')
    order           = models.IntegerField(verbose_name='Orden de presentación')
    active          = models.BooleanField(default=True, verbose_name='Activo')
    created         = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated         = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name        = 'Menú'
        verbose_name_plural = 'Menús'
        ordering            = ['order']

    def __str__(self):
        return self.title
    
class Food(models.Model):
    menu            = models.ForeignKey(Menu, verbose_name='Menú', on_delete=models.CASCADE)
    name            = models.CharField(max_length=100, verbose_name='Alimento')
    description     = models.CharField(max_length=100, verbose_name='Descripción')
    cost            = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Costo')
    previous_cost   = models.DecimalField(max_digits=4, decimal_places=2, verbose_name='Costo previo', null=True, blank=True)
    recommended     = models.BooleanField(default=False, verbose_name='Recomendado')
    order           = models.IntegerField(verbose_name='Order de presentación')
    created         = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    updated         = models.DateTimeField(auto_now=True, verbose_name='Fecha de actualización')

    class Meta:
        verbose_name        = 'Alimento'
        verbose_name_plural = 'Alimentos'
        ordering            = ['order']
    
    def __str__(self):
        return self.name
    

    


