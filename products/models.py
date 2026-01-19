import uuid
from django.db import models
from shared.models import BaseModel
from django.core.validators import  MinValueValidator ,  MaxValueValidator


class Product(BaseModel):
    product_code = models.CharField(max_length=6)
    product_name = models.CharField(max_length=64)


class Material(BaseModel):
    material_name = models.CharField(max_length=120)


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="products"
    )
    material_id = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="materials"
    )

class Warehouse(models.Model):
    material_id = models.OneToOneField(Material, on_delete=models.CASCADE , related_name='ware_house')
    remainder = models.IntegerField(
        validators=[
            MinValueValidator(1), 
            MaxValueValidator(1000)
        ]
    )
    price = models.IntegerField(
        [
            MinValueValidator(100),
            MaxValueValidator(100000)
        ]
    )
