from django.contrib import admin

from .models import Estoque


class EstoqueAdmin(admin.ModelAdmin):

    list_display = ['nome', 'slug', 'start_date', 'created_at']
    search_fields = ['nome', 'slug']
    prepopulated_fields = {'slug': ('nome',)}


admin.site.register(Estoque, EstoqueAdmin)
