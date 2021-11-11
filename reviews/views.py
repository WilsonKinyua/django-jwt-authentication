from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from .serializers import ProductSerializer
from .models import Product

# api
from django.http import JsonResponse
from rest_framework import status
from django.http import Http404
from rest_framework.response import Response

# jwt
from rest_framework.permissions import IsAuthenticated


class ProductViewSet(ReadOnlyModelViewSet):

    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    
    permission_classes = [IsAuthenticated] # jwt
    
    # add product 
    @action(detail=False, methods=['post'])
    def add_product(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False)
    def get_list(self, request):
        pass

    @action(detail=True)
    def get_product(self, request, pk=None):
        pass

    @action(detail=True, methods=['post', 'delete'])
    def delete_product(self, request, pk=None):
        pass
