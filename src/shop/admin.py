from django.contrib import admin
from .models import Category, Item

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Category, CategoryAdmin)

class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'stock', 'available', 'created_at', 'updated_at', 'price']
    list_filter = ['available', 'created_at', 'updated_at']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name', )}

admin.site.register(Item, ItemAdmin)
