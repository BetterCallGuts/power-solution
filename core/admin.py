from django.contrib import admin
from .models import Brand, Product, ProductImage, Category



class BrandAdmin(admin.ModelAdmin):
    list_display = ('name', 'thumb_nail' , "deactivated")
    search_fields = ('name',)
    list_filter = ('deactivated',)








class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0






class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',  "thumb_nail")
    search_fields = ('name',)
    inlines = [ProductImageInline]








admin.site.register(Brand  ,   BrandAdmin   )
admin.site.register(Product,   ProductAdmin )
admin.site.register(Category, )