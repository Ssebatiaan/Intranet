from django.contrib import admin

from .models import Comunicado


@admin.register(Comunicado)
class ComunicadoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'fijado', 'creado_en')
    list_filter = ('categoria', 'fijado')
    search_fields = ('titulo', 'contenido')
    date_hierarchy = 'creado_en'

    def save_model(self, request, obj, form, change):
        if not obj.autor_id:
            obj.autor = request.user
        super().save_model(request, obj, form, change)
