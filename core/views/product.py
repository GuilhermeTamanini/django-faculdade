from rest_framework.viewsets import ModelViewSet
from ..models import Product
from ..serializers import ProductSerializer

# from rest_framework.permissions import IsAuthenticatedOrReadOnly


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # permission_classes = (IsAuthenticatedOrReadOnly)


# class AvaliacaoViewSet(ModelViewSet):
#     queryset = Avaliacao.objects.all()
#     serializer_class = AvaliacaoSerializer
#     permission_classes = (IsAuthenticatedOrReadOnly,)
