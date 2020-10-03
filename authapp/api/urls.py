from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url, include
from authapp.api.views import *

app_name="authapp"

urlpatterns = [
    # djoser uygulaması ile login, register user ve get token işlemlerini sağlayacak url yönlendirmeleri
    path('',include('djoser.urls')), 
    path('',include('djoser.urls.authtoken')),
    ###
    path('games/',GameAPI.as_view(),name='games'),
    path('add-to-cart/',AddToCartAPI.as_view(),name='add-to-cart'),
    path('my-cart/',CartAPI.as_view(),name='my-cart'),
    path('checkout/',CheckOutAPI.as_view(),name='checkout'),
    path('orders/',OrderAPI.as_view(),name='orders'),
]