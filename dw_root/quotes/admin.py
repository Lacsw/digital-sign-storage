from django.contrib import admin
from .models import DigitalSign, Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'position', 'department', 'iogv')
    list_filter = ('position', 'department')
    search_fields = ('name',)
    # fieldsets = (
    #     (None, {
    #         'fields': ('name', 'last_name', 'iogv')
    #     }),
    #     ('Contact Information', {
    #         'classes': ('collapse',),
    #         'fields': ('position', 'department', 'email', 'work_phone', 'address')
    #     }),

    # )    

admin.site.register(Customer, CustomerAdmin)


#нид модель подписи
