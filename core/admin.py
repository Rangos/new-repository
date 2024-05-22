from django.contrib import admin
from core.models import *
from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.
class Loan_StatusImpExpAdmin(ImportExportModelAdmin):
    resources_classes = [Loan_Status]
    list_display = ['id', 'loan_status']

class Unit_Station_NamesImpExpAdmin(ImportExportModelAdmin):
    resources_classes = [Unit_Station_Names]
    list_display = ['id', 'unit_station_name', 'daily_target', 'monthly_target']

class LoansAdminImpExpAdmin(ImportExportModelAdmin):
    resources_classes = [Loans]
    list_display = ['id', 'loan_date', 'due_date', 'loan_code', 'loan_amount',
                    'customer_station', 'customer_id', 'loan_status']


admin.site.register(Loan_Status, Loan_StatusImpExpAdmin)
admin.site.register(Loans, LoansAdminImpExpAdmin)
admin.site.register(Unit_Station_Names, Unit_Station_NamesImpExpAdmin)
