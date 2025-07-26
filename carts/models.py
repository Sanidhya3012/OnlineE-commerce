from django.db import models
from store.models import Product, Variation

class Cart(models.Model):
    """
    Model representing a shopping cart.
    
    This model serves as a container for cart items and is typically
    associated with a session for anonymous users.
    
    Attributes:
        cart_id (str): Unique identifier for the cart (usually session ID)
        date_added (date): Date when the cart was created
    """
    cart_id = models.CharField(
        max_length=250,
        blank=True,
        help_text="Unique identifier for the cart (usually session ID)"
    )
    date_added = models.DateField(
        auto_now_add=True,
        help_text="Date when the cart was created"
    )

    def __str__(self):
        """String representation of the Cart"""
        return self.cart_id


class CartItems(models.Model):
    """
    Model representing items in a shopping cart.
    
    This model stores the relationship between products and carts,
    including quantity and variation selections.
    
    Attributes:
        product (Product): The product added to cart
        variations (ManyToManyField): Selected variations of the product
        cart (Cart): The cart containing this item
        quantity (int): Number of items
        is_active (bool): Whether the cart item is active
    """
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        help_text="The product added to cart"
    )
    variations = models.ManyToManyField(
        Variation,
        blank=True,
        help_text="Selected variations (size, color, etc.) of the product"
    )
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE,
        help_text="The cart containing this item"
    )
    quantity = models.IntegerField(
        help_text="Number of items"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether the cart item is active"
    )

    def sub_total(self):
        """
        Calculate the subtotal for this cart item.
        
        Returns:
            float: The product of item price and quantity
        """
        return self.product.price * self.quantity

    def __str__(self):
        """String representation of the CartItem"""
        return f"{self.product.product_name} ({self.quantity})"
