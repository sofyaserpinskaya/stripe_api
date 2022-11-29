from django.db import models


class Order(models.Model):
    pass


class Item(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.PositiveIntegerField()
    orders = models.ManyToManyField(
        Order,
        related_name='items',
        blank=True,
    )

    class Meta():
        ordering = ('id',)

    def __str__(self):
        return f'{self.name[:15]} - {self.price}'
