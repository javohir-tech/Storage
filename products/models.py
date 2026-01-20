import uuid
from django.db import models
from shared.models import BaseModel
from django.core.validators import MinValueValidator, MaxValueValidator


class Product(BaseModel):
    product_code = models.IntegerField(unique=True)
    product_name = models.CharField(max_length=64, unique=True)

    def create_material(self, material, quantity):
        material_quantity = ProductMaterial(
            product_id=self, material_id=material, quantity=quantity
        )

    def check_product_name(self):
        if self.product_name:
            self.product_name = self.product_name.lower().strip()

    def save(self, *args, **kwargs):
        self.check_product_name()

        super().save(*args, **kwargs)

    def __str__(self):
        return self.product_name


class Material(BaseModel):
    material_name = models.CharField(max_length=120, unique=True)

    def check_material_name(self):
        if self.material_name:
            self.material_name = self.material_name.lower().strip()

    def __str__(self):
        return self.material_name

    def save(self, *args, **kwargs):
        self.check_material_name()

        super().save(*args, **kwargs)


class ProductMaterial(models.Model):
    product_id = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="materials"
    )
    material_id = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="products"
    )
    quantity = models.DecimalField(max_digits=10, decimal_places=2)


class Warehouse(models.Model):
    material_id = models.ForeignKey(
        Material, on_delete=models.CASCADE, related_name="ware_house"
    )
    remainder = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(1000)]
    )
    price = models.IntegerField(
        validators=[MinValueValidator(100), MaxValueValidator(100000)]
    )
