from rest_framework.generics import ListAPIView,ListCreateAPIView
from rest_framework import generics
from rest_framework import filters
from authapp.models import *
from authapp.api.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes,action

# Oyun nesnelerini listeyen view
@permission_classes([IsAuthenticated])
class GameAPI(generics.ListAPIView):
    queryset = Game.objects.all()
    serializer_class = GameSerializer

    # rest_framework'ün filters methodu sayesinde ve generics yapısını kullanarak 
    # dinamik filtreleme sağlanabiliyor
    search_fields = ['name','category']
    filter_backends = (filters.SearchFilter,)


# Sepete ekleme viewı
@permission_classes([IsAuthenticated])
class AddToCartAPI(generics.ListCreateAPIView):
    queryset = Cart.objects.all()
    serializer_class = AddToCartSerializer

    # Kullanıcı sadece kendi viewlerını görüntüleyebilir
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)

    # Eklenen nesnenin user özelliğine otomatik olarak isteği yollayan kullanıcı atanır
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)

# Sepetteki ürünleri listeleyen view
@permission_classes([IsAuthenticated])
class CartAPI(generics.ListAPIView):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer

    # Kullanıcı sadece kendi viewlerını görüntüleyebilir
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)


# Sepetteki ürünleri siparişe dönüştüren view
@permission_classes([IsAuthenticated])
class CheckOutAPI(generics.ListAPIView):
    
    # Post methodu geldiğinde
    @action(detail=False, methods=['post'])
    def post(self, request):

        # Kullanıcının sepetindeki ürünleri al
        carts = Cart.objects.filter(user=self.request.user)

        # Sepet boş ise
        if len(carts)==0:
            return Response('Sepetiniz Boş.')

        # Sipariş oluşturur   
        check_request = CheckOut()
        check_request.user = self.request.user
        check_request.save()
        for i in carts:
            check_request.games.add(i.game)
        
        #Siparişleri aldıktan sonra sepeti boşaltır
        Cart.objects.filter(user=self.request.user).delete()

        return Response('Siparişiniz başarıyla alınmıştır.')

    queryset = CheckOut.objects.all()
    serializer_class = CheckOutSerializer


# Siparişleri görüntüleyecek view
@permission_classes([IsAuthenticated])
class OrderAPI(generics.ListAPIView):
    queryset = CheckOut.objects.all()
    serializer_class = OrdersSerializer

    def get_queryset(self):
        return CheckOut.objects.filter(user=self.request.user)
   
