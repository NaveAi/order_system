from django.db import models
from django.contrib.auth.models import User

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    details = models.TextField()
    status = models.CharField(max_length=50, default="ההזמנה התקבלה")

    def __str__(self):
        return f"Order #{self.id} by {self.user.username}"