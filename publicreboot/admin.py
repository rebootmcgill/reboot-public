from django.contrib import admin
from publicreboot.models import OfficeHours, Holiday
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
# Register your models here.
admin.site.register(OfficeHours)

class HolidayFilter(admin.SimpleListFilter):
    title = _('Holiday Timeframe')
    parameter_name = 'timeframe'
    def lookups(self, request, model_admin):
        return (
            ('past', _('Past Holidays')),
            ('now', _('Current Holidays')),
            ('future',_('Future Holidays')),
        )
    def queryset(self, request, queryset):
        today = timezone.now().date
        if self.value() == 'past':
            return queryset.filter(end_date__lte=today)
        if self.value() == 'now':
            return queryset.filter(start_date__lte=today, end_date__gte=today)
        if self.value() == 'future':
            return queryset.filter(start_date__gte=today)

@admin.register(Holiday)
class HolidayAdmin(admin.ModelAdmin):
    date_hierarchy = 'start_date'
    list_display = ('name', 'start_date', 'end_date')
    list_filter = (HolidayFilter,)
    fieldsets = (
        (None, {'fields': ('name',)}),
        ('Dates', {'fields': ('start_date', 'end_date')}),
    )
