from django.contrib import admin
from .models import Documents, KeyInformation

# Register your models here.


@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


@admin.register(KeyInformation)
class KeyInformationAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
