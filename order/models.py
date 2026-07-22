from django.db import models

# Create your models here.
class Client(models.Model):

    name = models.CharField(max_length=50)
    email= models.EmailField(max_length=254, unique=True)

    class Meta:
        verbose_name = "client"
        verbose_name_plural = "clients"

    def __str__(self):
        
        return self.name

class Product(models.Model):

    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField()
    

    class Meta:
        verbose_name = "product"
        verbose_name_plural = "products"

    def __str__(self):
        return self.name

class Order(models.Model):
    
    STATUS_ORDER = {
        "PENDING":"pending", 
        "CANCELED":"aborded",
        "DELIVERED":"delivered"
    }
    client = models.ForeignKey("Client", related_name="orders", on_delete=models.CASCADE)
    order_date = models.DateField(auto_now=False, auto_now_add=True)
    status = models.CharField(max_length=50, choices=STATUS_ORDER, default=STATUS_ORDER["PENDING"])

    class Meta:
        verbose_name = "order"
        verbose_name_plural = "orders"

    def __str__(self):
        return f"{self.client.name} on {self.order_date}"

class OrderLine(models.Model):

    order = models.ForeignKey("Order", on_delete=models.CASCADE, related_name="products_orders")
    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="order_lines")
    quantity = models.PositiveIntegerField()
    unit_price = models.DecimalField(max_digits=8, decimal_places=2)

    class Meta:
        verbose_name = "OrderLine"
        verbose_name_plural = "OrderLines"
        constraints=[
            models.UniqueConstraint(fields=['order','product'],name="unique_product_order")
        ]

    def __str__(self):
        return f"{self.product.name} X {self.quantity} - {self.unit_price}"
