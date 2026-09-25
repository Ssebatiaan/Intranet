from django.conf import settings
from django.db import models
from django.urls import reverse


class Comunicado(models.Model):
    """Un aviso o noticia publicada en la intranet."""

    class Categoria(models.TextChoices):
        GENERAL = 'general', 'General'
        RRHH = 'rrhh', 'Recursos humanos'
        TI = 'ti', 'Tecnología'
        EVENTOS = 'eventos', 'Eventos'

    titulo = models.CharField('título', max_length=200)
    contenido = models.TextField('contenido')
    categoria = models.CharField(
        'categoría', max_length=20, choices=Categoria.choices, default=Categoria.GENERAL
    )
    autor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        verbose_name='autor',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='comunicados',
    )
    fijado = models.BooleanField('fijado', default=False, help_text='Mostrar siempre arriba')
    creado_en = models.DateTimeField('creado', auto_now_add=True)
    actualizado_en = models.DateTimeField('actualizado', auto_now=True)

    class Meta:
        verbose_name = 'comunicado'
        verbose_name_plural = 'comunicados'
        ordering = ['-fijado', '-creado_en']

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse('comunicado_detalle', args=[self.pk])
