from django.db import models

# Create your models here.
class Sales(models.Model):
    product = models.CharField(max_length=255)
    price = models.IntegerField()
    currency = models.CharField(
        choices=(('USD', 'USD'), ('EUR', 'EUR')),
        default='USD',
        max_length=3
    )
    country = models.CharField(max_length=50)
    purchase_date = models.DateTimeField()


    def __str__(self):
        return self.product


    class Meta:
        verbose_name = 'Sale'
        verbose_name_plural = 'Sales'

