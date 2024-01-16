from django.contrib import admin
from .models import Profit, Expenditure
from import_export import resources
from import_export.admin import ImportExportModelAdmin

@admin.register(Profit)
class ProfitAdmin(ImportExportModelAdmin):
    list_display = ('id', 'quantity', 'date', 'fk_sale_id')
    list_editable = ('quantity',)  
    search_fields = ('quantity', 'date', 'fk_sale__id') 
    list_filter = ('date', 'fk_sale__id')  
    ordering = ['id']
    
@admin.register(Expenditure)
class ExpenditureAdmin(ImportExportModelAdmin):
    list_display = ('id', 'quantity', 'description', 'fecha', 'fk_product_id')
    list_editable = ('quantity',) 
    search_fields = ('quantity', 'description', 'fecha', 'fk_product__id')  
    list_filter = ('fk_product__id',) 
    ordering = ['id']

class ProfitResource(resources.ModelResource):
    class Meta:
        model = Profit
        fields = ('quantity', 'date', 'fk_sale_id')

class ExpenditureResource(resources.ModelResource):
    class Meta:
        model = Expenditure
        fields = ('quantity', 'description', 'fecha', 'fk_product_id')