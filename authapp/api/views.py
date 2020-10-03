from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework import generics
from rest_framework import filters
from authapp.models import *
from authapp.api.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,action

@permission_classes([IsAuthenticated])
class GameAPI(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    search_fields = ['name','category']
    filter_backends = (filters.SearchFilter,)


@permission_classes([IsAuthenticated])
class AddToCartAPI(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = AddToCartSerializer

    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

@permission_classes([IsAuthenticated])
class CartAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


@permission_classes([IsAuthenticated])
class CheckOutAPI(generics.ListAPIView):
    
    @action(detail=False, methods=['post'])
    def post(self, request):
        carts = Cart.objects.filter(user=self.request.user)
        if len(carts)==0:
            return Response('Sepetiniz Boş.')
        check_request = CheckOut()
        check_request.user = self.request.user
        check_request.save()
        for i in carts:
            check_request.games.add(i.game)
        
        Cart.objects.filter(user=self.request.user).delete()
        return Response('Başarılı')

    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer


@permission_classes([IsAuthenticated])
class OrderAPI(generics.ListAPIView):
    queryset = CheckOut.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return CheckOut.objects.filter(user=self.request.user)
   
