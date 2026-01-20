# //////////////// Django ///////////////////////////
from django.shortcuts import render

# //////////////  REST FRAMEWORK ///////////////////
from rest_framework.views import APIView
from rest_framework.validators import ValidationError
from rest_framework.response import Response
from rest_framework import status

# /////////////    Serializers /////////////////////
from .serializers import ProductMaterialListSerializer, PartiyaSerializer

# ////////////////// Models /////////////////////
from .models import Product, Material, ProductMaterial, Warehouse


class ProductMaterailListView(APIView):

    def post(self, request):
        serializer = ProductMaterialListSerializer(data=request.data, many=True)

        serializer.is_valid(raise_exception=True)
        print("=" * 50)
        print(serializer.validated_data)
        print("=" * 50)
        resault = []
        for data in serializer.validated_data:
            try:
                p_code = data.get("product_code")
                quantity = data.get("quantity")
                product = Product.objects.filter(product_code=p_code).first()
                product_materials = product.materials.all()
                print("=" * 50)
                product_materials_result = []
                for product_material in product_materials:
                    need_matrail = quantity * product_material.quantity
                    material = Material.objects.get(id=product_material.material_id_id)
                    warehouse = material.ware_house.all()
                    qty = 0
                    partiya_permission = True
                    print(partiya_permission)
                    for partiya in warehouse:
                        remainder = need_matrail - partiya.remainder
                        if remainder <= 0:
                            qty = need_matrail
                            need_matrail = 0
                        elif remainder >= 0:
                            qty = partiya.remainder
                            need_matrail = need_matrail - qty

                        partiya_data = {
                            "warehouse_id": partiya.id,
                            "material_name": material.material_name,
                            "qty": qty,
                            "price": partiya.price,
                        }

                        partiya_serializer = PartiyaSerializer(data=partiya_data)
                        partiya_serializer.is_valid(raise_exception=True)
                        product_materials_result.append(
                            partiya_serializer.validated_data
                        )
                        print(partiya_serializer.validated_data)

                    print(material)
                    print(need_matrail)
                print("=" * 50)
                product_name = product.product_name
                temp_data = {
                    "product_name": product_name,
                    "product_qty": quantity,
                    "product_materials": product_materials_result,
                }
                resault.append(temp_data)
                # resault.append(temp_data)
            except Exception as e:
                raise ValidationError(f"{e}")

        print("=" * 50)
        print(resault)
        print("=" * 50)
        return Response({"result": resault}, status=status.HTTP_200_OK)
