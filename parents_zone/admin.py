from django.contrib import admin
from .models import ParentsInformation

# Register your models here.


class ParentsInformationAdmin(admin.ModelAdmin):
    readonly_fields = ["created", "updated"]


admin.site.register(ParentsInformation, ParentsInformationAdmin)
