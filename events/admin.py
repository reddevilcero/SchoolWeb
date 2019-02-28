from django.contrib import admin
from .models import Event, EventImage

# Register your models here.


class EventImageInline(admin.TabularInline):
    model = EventImage
    extra = 3


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    readonly_fields = ['created', 'updated']
    inlines = [EventImageInline]
