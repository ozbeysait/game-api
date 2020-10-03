from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authapp.models import *


# Oyun nesneleriyle ilgili serializer
class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


# Sepet ile ilgili serializer
class CartSerializer(ModelSerializer):
    # Sepette listelenirken id yerine ismi ile görüntülenmesini sağlar
    game_name = serializers.SerializerMethodField(method_name='new_name')
    def new_name(self,obj):
        return str(obj.game)
        
    class Meta:
        model = Cart
        fields = ('game_name','created_date',)
    
    
# Sepette ekleme işlemlerinde kullanılan serializer
class AddToCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('game',)
    
    # Oyunun sepete daha önce eklenip eklenmediğini kontrol eder
    def validate(self,attrs):
        queryset = Cart.objects.filter(game=attrs["game"])
        if queryset.exists():
            raise serializers.ValidationError("Eklemeye çalıştığınız ürün sepette mevcut.")
        return attrs


# Sepetteki oyunların siparişe dönüşmesini sağlayan serializer
class CheckOutSerializer(ModelSerializer):
    game_name = serializers.SerializerMethodField(method_name='new_name')
    def new_name(self,obj):
        return str(obj.game)

    # Sepet nesnesi ile Checkout modellerini ilişkilendirir
    cart = CartSerializer(read_only=True,many=True)

    class Meta:
        model = CheckOut
        fields = ('game_name',)


# Önceki siparişlerin görüntüleyen serializer
class OrdersSerializer(ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ('games','created_date',)



    