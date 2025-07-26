from django.db import models
from django.urls import reverse

class Category(models.Model):
    """
    Model representing a product category in the e-commerce system.
    
    This model stores information about product categories, including their names,
    URL-friendly slugs, descriptions, and optional category images.
    
    Attributes:
        category_name (str): The name of the category (unique)
        slug (str): URL-friendly version of the category name (unique)
        description (str): Optional description of the category
        cat_image (ImageField): Optional category image
    """
    
    category_name = models.CharField(
        max_length=50,
        unique=True,
        help_text="Enter the category name (must be unique)"
    )
    
    slug = models.SlugField(
        max_length=100,
        unique=True,
        help_text="URL-friendly version of the category name"
    )
    
    description = models.TextField(
        max_length=255,
        blank=True,
        help_text="Optional description of the category"
    )
    
    cat_image = models.ImageField(
        upload_to='photos/categories',
        blank=True,
        help_text="Optional category image"
    )

    class Meta:
        """
        Meta options for the Category model.
        Specifies the verbose names for admin interface.
        """
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_url(self):
        """
        Generate the URL for viewing products in this category.
        
        Returns:
            str: URL path for viewing products in this category
        """
        return reverse('products_by_category', args=[self.slug])

    def __str__(self):
        """
        String representation of the Category.
        
        Returns:
            str: The category name
        """
        return self.category_name
