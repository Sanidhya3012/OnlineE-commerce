from django.db import models
from category.models import Category
from django.urls import reverse

class Product(models.Model):
    """
    Model representing a product in the e-commerce system.
    
    This model stores all product-related information including name, price,
    stock levels, and availability status.
    
    Attributes:
        product_name (str): Name of the product (unique)
        slug (str): URL-friendly version of the product name (unique)
        description (str): Detailed description of the product
        price (int): Price of the product
        images (ImageField): Product images
        stock (int): Current stock level
        is_available (bool): Product availability status
        category (Category): Foreign key to Category model
        created_date (datetime): When the product was created
        modified_date (datetime): When the product was last modified
    """
    product_name    = models.CharField(max_length=200, unique=True)
    slug            = models.SlugField(max_length=200, unique=True)
    description     = models.TextField(max_length=500, blank=True)
    price           = models.IntegerField()
    images          = models.ImageField(upload_to='photos/products')
    stock           = models.IntegerField()
    is_available    = models.BooleanField(default=True)
    category        = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date    = models.DateTimeField(auto_now_add=True)
    modified_date   = models.DateTimeField(auto_now=True)

    def get_url(self):
        """
        Generate the URL for viewing this product's detail page.
        
        Returns:
            str: URL path for the product detail view
        """
        return reverse('product_detail', args=[self.category.slug, self.slug])

    def __str__(self):
        """String representation of the Product"""
        return self.product_name


class VariationManager(models.Manager):
    """
    Custom manager for handling product variations.
    Provides methods to filter variations by category (color/size).
    """
    
    def colors(self):
        """
        Get all active color variations.
        
        Returns:
            QuerySet: Active color variations
        """
        return super(VariationManager, self).filter(variation_category='color', is_active=True)

    def sizes(self):
        """
        Get all active size variations.
        
        Returns:
            QuerySet: Active size variations
        """
        return super(VariationManager, self).filter(variation_category='size', is_active=True)


# Choices for variation categories
variation_category_choice = (
    ('color', 'color'),
    ('size', 'size'),
)


class Variation(models.Model):
    """
    Model representing product variations (e.g., sizes, colors).
    
    This model handles different variations of products such as different
    colors or sizes available for the same product.
    
    Attributes:
        product (Product): The base product this variation belongs to
        variation_category (str): Type of variation (color/size)
        variation_value (str): Specific value of the variation
        is_active (bool): Whether this variation is currently active
        created_date (datetime): When the variation was created
    """
    product             = models.ForeignKey(Product, on_delete=models.CASCADE)
    variation_category  = models.CharField(
        max_length=100,
        choices=variation_category_choice,
        help_text="Type of variation (color or size)"
    )
    variation_value     = models.CharField(
        max_length=100,
        help_text="Specific value for this variation"
    )
    is_active           = models.BooleanField(default=True)
    created_date        = models.DateTimeField(auto_now=True)

    # Use the custom manager
    objects = VariationManager()

    def __str__(self):
        """String representation of the Variation"""
        return self.variation_value
