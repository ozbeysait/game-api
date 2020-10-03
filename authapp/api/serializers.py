from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from authapp.models import *

class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class CartSerializer(ModelSerializer):
    game_name = serializers.SerializerMethodField(method_name='new_name')
    class Meta:
        model = Cart
        fields = ('game_name','created_date',)
    
    def new_name(self,obj):
        return str(obj.game)

class AddToCartSerializer(ModelSerializer):
    class Meta:
        model = Cart
        fields = ('game',)
    
    def validate(self,attrs):
        queryset = Cart.objects.filter(game=attrs["game"])
        if queryset.exists():
            raise serializers.ValidationError("Eklemeye çalıştığınız ürün sepette mevcut.")
        return attrs


class CheckOutSerializer(ModelSerializer):
    game_name = serializers.SerializerMethodField(method_name='new_name')
    cart = CartSerializer(read_only=True,many=True)
    class Meta:
        model = CheckOut
        fields = ('game_name',)

    def new_name(self,obj):
        return str(obj.game)

class OrdersSerializer(ModelSerializer):
    class Meta:
        model = CheckOut
        fields = ('games','created_date',)



    