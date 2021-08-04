from django.contrib import admin
from .models import DigitalSign, Customer

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'last_name', 'position', 'department', 'iogv')
    list_filter = ('position', 'department')
    readonly_fields = ('submitted',)
    search_fields = ('name',)
    fieldsets = (
        (None, {
            'fields': ('name', 'last_name', 'iogv')
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('position', 'department', 'email', 'work_phone', 'address')
        }),
        ('Job Information', {
            'classes': ('collapse',),
            'fields': ('sitestatus', 'priority', 'jobfile', 'submitted')
        }),
    )    

admin.site.register(Customer, CustomerAdmin)

