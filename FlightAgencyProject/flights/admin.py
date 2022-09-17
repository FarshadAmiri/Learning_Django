from django.contrib import admin
from .models import *
from django.contrib import admin, messages
import datetime as dt

admin.site.register(City)
admin.site.register(Airport)
admin.site.register(Airline)


def custom_titled_filter(title):
    class Wrapper(admin.FieldListFilter):
        def __new__(cls, *args, **kwargs):
            instance = admin.FieldListFilter.create(*args, **kwargs)
            instance.title = title
            return instance
    return Wrapper



@admin.register(Flight)
class FlightAdmin(admin.ModelAdmin):
    def flight_date(self, obj):
        return obj.datetime.strftime("%Y/%m/%d  %H:%M")
    list_display = ('pk', 'str2', 'flight_date','airline')
    list_display_links = ['pk', 'str2']
    ordering = ['datetime']
    list_filter = [('origin__city', custom_titled_filter('origin__city')), ('destination__city', custom_titled_filter('destination__city')), 'airline']
    search_fields = ['origin__city__name', 'destination__city__name']
    # list_editable = ['airline']
    readonly_fields = ['airline']
    # date_hierarchy = 'datetime'

    fieldsets = (
        ("Flight's General Information", {
            'fields':('origin', 'destination')
        }),
        ('More info' , {
            'classes':('collapse',), 'fields':('airline', 'datetime')
        }),
    )

    def shift_by_2hours(self, request, queryset):
        for f in queryset:
            f.datetime = f.datetime + dt.timedelta(hours=2)
            f.save()
        self.message_user(
            request, f"{queryset.count()} flights shifted by 2 hours", messages.SUCCESS
        )

    actions = ['shift_by_2hours']
    shift_by_2hours.short_description = 'Postpone flight(s) for 2 hours'


@admin.register(Passenger)
class PassengerAdmin(admin.ModelAdmin):
    list_display = ['national_id','__str__',]
    list_display_links = ['national_id','__str__',]
    # filter_horizontal = ('tickets',)




