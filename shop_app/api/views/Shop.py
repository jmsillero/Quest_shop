from rest_framework import viewsets

from shop_app.models import Shop
from shop_app.serializer import ShopSerializer
from rest_framework import permissions


class ShopViewSet(viewsets.ModelViewSet):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def shop_create(self, serializer):
        serializer.save(owner=self.request.user)