from django.contrib import admin
from .models import Tutor, Slide

# Register your models here.


class TutorAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


class SlideAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Tutor, TutorAdmin)
admin.site.register(Slide, SlideAdmin)
