from .models import Product
from .serializers import ProductSerializer

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response


class ProductSearchAPIView(APIView):

    def post(self, request, format=None):
        '''
        POST /product/
        optional payload
        {
            'offset': int (default 0),
            'products_per_page': int (default 10)
        }
        '''
        offset = 0
        products_per_page = 10
        if 'offset' in request.data:
            offset = int(request.data.get('offset'))
        if 'products_per_page' in request.data:
            products_per_page = int(request.data['products_per_page']
        # First getting all products
        all_products = Product.objects.all()
        if all_products:
            # Using list slicing to create the page itens
            paginated_products = all_products[offset:(offset+products_per_page)]
            # Serializing my itens
            serializer = ProductSerializer(paginated_products, many=True)
            # Returning the response data
            return Response(serializer.data)
        else:
            return Response([])
