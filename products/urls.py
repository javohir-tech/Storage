from django.urls import path
from .views import ProductMaterailListView

urlpatterns = [path("materials/", ProductMaterailListView.as_view())]
