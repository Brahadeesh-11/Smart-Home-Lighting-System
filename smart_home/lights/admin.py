from django.contrib import admin
from .models import Light

@admin.register(Light)
class LightAdmin(admin.ModelAdmin):
    list_display = ('light_id', 'name', 'status')
