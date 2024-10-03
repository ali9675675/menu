from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Item(models.Model):

    def __str__(self):
        return self.item_name
    user_name = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    item_name = models.CharField(max_length=200)
    item_description = models.TextField()
    item_price = models.PositiveIntegerField()
    item_image = models.CharField(max_length=500, default='https://www.theaxebraughing.uk/wp-content/uploads/2020/04'
                                                          '/food-placeholder-image.jpg')

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})
