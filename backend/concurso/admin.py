from django.contrib import admin

# Register your models here.

from .models import Participante
@admin.register(Participante)
class ParticipanteAdmin(admin.ModelAdmin):
    list_display = ('email', 'nombre_completo', 'verificado', 'es_participante', 'es_ganador', 'fecha_inscripcion')
    search_fields = ('email', 'nombre_completo')
    list_filter = ('verificado', 'es_participante', 'es_ganador', 'fecha_inscripcion')
    ordering = ('-fecha_inscripcion',)
