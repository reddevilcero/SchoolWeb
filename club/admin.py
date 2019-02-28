from django.contrib import admin
from .models import Club

# Register your models here.


class ClubAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')


admin.site.register(Club, ClubAdmin)
