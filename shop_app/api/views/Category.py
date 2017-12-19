from rest_framework import viewsets
from shop_app.serializer import CategorySerializer
from shop_app.models import Category

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


