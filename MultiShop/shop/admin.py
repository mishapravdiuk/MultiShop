from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.

class ProductImageAdmin(admin.StackedInline):
    model=ProductImage


@admin.register(ProductInfo)
class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    save_as=True
    save_on_top=True
    list_display = ('title', 'slug',  'color', 'category', 'price', 'quantity', 'views', 'get_photo')
    list_display_links=('title', 'slug')
    search_fields=('title',)
    list_filter=('category',)
    readonly_fields= ('views',)
    fields=('title', 'slug',  'color', 'size', 'category', 'description', 'price', 'quantity', 'views', 'photo')
    inlines = [ProductImageAdmin]


    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'

    get_photo.short_description = "Photo"

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    fields=('title', 'slug', 'photo')
    search_fields=('title',)
    list_display_links=('title', 'slug')
    list_display = ('title', 'slug')
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
