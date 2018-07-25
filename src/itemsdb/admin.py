from django.contrib import admin

from . import models


class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'category', 'code', 'name', 'active'
    )
    list_filter = ('created', 'category')


class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'slug', 'name',
    )
    list_filter = ('created',)
    prepopulated_fields = {'slug': ('name',)}


def _register(model, admin_class):
    admin.site.register(model, admin_class)


_register(models.Category, CategoryAdmin)
_register(models.Item, ItemAdmin)
