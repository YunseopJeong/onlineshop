from django.contrib import admin
from .models import *

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    # 관리자 화면생성
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug':('name',)}

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'category', 'price', 'stock', 'available_display', 'available_order', 'created', 'updated']
    prepopulated_fields = {'slug': ('name',)}
    list_filter = ['available_display', 'created', 'updated', 'category']
    list_editable = ['price', 'stock', 'available_display', 'available_order']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)