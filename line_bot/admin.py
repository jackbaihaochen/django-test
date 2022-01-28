from django.contrib import admin
from line_bot.models import LineAuthInfo


# Register your models here.
@admin.register(LineAuthInfo)
class LineAuthInfoAdmin(admin.ModelAdmin):
    list_display = ('key', 'value')