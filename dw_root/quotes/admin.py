from quotes.forms import DigitalSignForm
from django.contrib import admin

from .models import DigitalSign, Customer, GisNumber


class DigitalSignInline(admin.TabularInline):
    """Добавляет пользователю все связанные сертификаты на страницу"""
    model = DigitalSign
    extra = 0


class CustomerAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'name', 'position', 'department', 'iogv')
    list_filter = ('position', 'department')
    search_fields = ('name',)
    inlines = [DigitalSignInline]
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


@admin.register(DigitalSign)
class DigitalSignAdmin(admin.ModelAdmin):
    list_display = ('customer', 'sign_type',
                    'start_date', 'end_date',)
    list_filter = ('customer', 'end_date')
    search_fields = ('customer', 'start_date', 'end_date')

    # fields = ['customer', 'sign_type', ('start_date', 'end_date'), 'status']


admin.site.register(GisNumber)
