from django.db import models
from django.conf import settings

# Oyun modeli
class Game(models.Model):
    CATEGORIES = (
        ('Futbol','Futbol'),
        ('Dövüş','Dövüş'),
        ('Basketbol','Basketbol'),
        ('Platform','Platform'),
        ('Planet','Planet'),
    )
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    category = models.CharField(max_length=50,choices=CATEGORIES)

    def __str__(self):
        return self.name

# Sepet modeli
class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    game = models.ForeignKey(Game,on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

# Siparişlerle ilişkilendirilecek model
class CheckOut(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    games = models.ManyToManyField(Game)
    created_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.user.username

