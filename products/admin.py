from django.contrib import admin
from .models import Product, Material, ProductMaterial, Warehouse


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ["id", "product_name", "product_code"]
    search_fields = ["product_name"]


@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ["id", "material_name"]
    search_fields = ["material_name"]


@admin.register(ProductMaterial)
class ProductMaterialAdmin(admin.ModelAdmin):
    list_display = ["product_id", "material_id" , "quantity"]


@admin.register(Warehouse)
class WareHouseAdmin(admin.ModelAdmin):
    list_display = ["id", "remainder", "price"]


# Register your models here.
