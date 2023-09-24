from django.db import models

# Create your models here.

class Expenses(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()

    class Meta:
        verbose_name = "Expenses"
        verbose_name_plural = "Expenses"

    def __str__(self):
        return self.name