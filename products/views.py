from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import ProductMaterialListSerializer


class ProductMaterailListView(APIView):

    def post(self, request):
        serializer = ProductMaterialListSerializer(data=request.data)



