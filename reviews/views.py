from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from .serializers import ProductSerializer
from .models import Product


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()

    @action(detail=False)
    def get_list(self, request):
        pass

    @action(detail=False)
    def get_product(self, request, pk=None):
        pass

    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass
