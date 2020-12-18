from django.contrib import admin
from .models import Send

@admin.register(Send)
class Sendadmin(admin.ModelAdmin):
    list_display = ("email",)
    list_filter = ("email", )
