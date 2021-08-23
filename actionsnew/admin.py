from django.contrib import admin
from django.contrib import admin
from .models import ActionNew


@admin.register(ActionNew)
class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'verb', 'target', 'created')
    list_filter = ('created',)
    search_fields = ('verb',)


# Register your models here.
