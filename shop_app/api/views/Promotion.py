from rest_framework import viewsets
from shop_app.models import Promotion
from shop_app.serializer import PromotionSerializer

class PromotionViewSet(viewsets.ModelViewSet):
    queryset = Promotion.objects.all()
    serializer_class = PromotionSerializer