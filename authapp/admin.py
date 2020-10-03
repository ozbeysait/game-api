from django.contrib import admin
from .models import *

#Modellerin admin paneline eklenmesi
admin.site.register(Game)
admin.site.register(Cart)
admin.site.register(CheckOut)