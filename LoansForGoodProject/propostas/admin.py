from django.contrib import admin
from .models import Proposta, CampoPersonalizado

class CampoPersonalizadoInline(admin.TabularInline):
    model = CampoPersonalizado

class PropostaAdmin(admin.ModelAdmin):
    list_display = ('document', 'name', 'status')
    list_filter = ('status',)
    inlines = [CampoPersonalizadoInline]
    actions = ['aprovar_propostas', 'negar_propostas']

    def aprovar_propostas(self, request, queryset):
        queryset.update(status='Aprovada')
    aprovar_propostas.short_description = 'Aprovar propostas selecionadas'

    def negar_propostas(self, request, queryset):
        queryset.update(status='Negada')
    negar_propostas.short_description = 'Negar propostas selecionadas'




admin.site.register(Proposta, PropostaAdmin)
