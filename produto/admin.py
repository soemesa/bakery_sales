from django.contrib import admin
from . import models


class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome', 'descricao',
                    'get_preco_formatado', 'get_preco_promocional_formatado']


admin.site.register(models.Produto, ProdutoAdmin)
