from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import *

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    save_as=True
    list_display = ('title', 'slug',  'color', 'category', 'price', 'quantity', 'views', 'get_photo')
    list_display_links=('title', 'slug')
    list_filter=('category',)
    readonly_fields= ('views',)
    fields=('title', 'slug',  'color', 'size', 'category', 'description', 'price', 'quantity', 'views', 'photo')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        else:
            return '-'


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields ={"slug": ('title',)}
    


admin.site.register(Category, CategoryAdmin)
admin.site.register(Size)
admin.site.register(ProductInfo, ProductAdmin)

