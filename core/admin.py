from django.contrib import admin
from .models import Brand, Product, ProductImage, Category, RequestInfo, Page, ProductHighLight, Ferbo


class BrandAdmin(admin.ModelAdmin):
    list_display  = ('name', 'thumb_nail' , "deactivated")
    search_fields = ('name',)
    list_filter   = ('deactivated',)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductHighLightInline(admin.TabularInline):
    model = ProductHighLight
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display  = ('name', 'description',  "thumb_nail")
    search_fields = ('name',)
    inlines       = [ProductImageInline, ProductHighLightInline]



class RequestInfoAdminStyle(admin.ModelAdmin):
    list_display  = ('name', 'email', 'phone', 'company', 'description', )
    search_fields = ('name',)
    list_filter   = ("prod",)


admin.site.register(Brand  ,   BrandAdmin   )
admin.site.register(Product,   ProductAdmin )
admin.site.register(RequestInfo, RequestInfoAdminStyle)


admin.site.register(Category, )
admin.site.register(Page)
admin.site.register(Ferbo)