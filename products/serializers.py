from rest_framework import serializers
from rest_framework.validators import ValidationError
from .models import Product, Warehouse


class ProductMaterialListSerializer(serializers.Serializer):
    product_code = serializers.IntegerField()
    quantity = serializers.IntegerField()

    def validate(self, attrs):

        p_code = attrs.get("product_code")
        product = Product.objects.filter(product_code=p_code)
        if not product.exists():
            raise ValidationError(
                {"success": False, "message": f"{p_code} product bazada mavjud emas"}
            )

        return attrs


class PartiyaSerializer(serializers.Serializer):
    warehouse_id = serializers.IntegerField(allow_null=True)
    material_name = serializers.CharField()
    qty = serializers.IntegerField()
    price = serializers.IntegerField(allow_null=True)
