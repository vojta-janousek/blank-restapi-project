from django.contrib import admin

from status.models import Status
from status.forms import StatusForm

# Register your models here.
class StatusAdmin(admin.ModelAdmin):
    list_display = ['user', '__str__', 'image']
    form = StatusForm


admin.site.register(Status, StatusAdmin)
