from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
# Create your models here.


class MyAccountManager(BaseUserManager):
    """
    Custom account manager for the Account model.
    Extends Django's BaseUserManager to provide methods for creating users and superusers.
    """
    
    def create_user(self, first_name, last_name, username, email, password=None):
        """
        Creates and saves a new user with the given details.
        
        Args:
            first_name (str): User's first name
            last_name (str): User's last name
            username (str): Unique username
            email (str): User's email address
            password (str, optional): User's password
            
        Returns:
            Account: Created user instance
            
        Raises:
            ValueError: If email or username is not provided
        """
        if not email:
            raise ValueError('User must have an email address')

        if not username:
            raise ValueError('User must have an username')

        # Create a new user instance
        user = self.model(
            email       = self.normalize_email(email),  # Normalize email to lowercase domain
            username    = username,
            first_name  = first_name,
            last_name   = last_name,
        )

        user.set_password(password)  # Hash the password
        user.save(using=self._db)
        return user

    def create_superuser(self, first_name, last_name, email, username, password):
        """
        Creates and saves a new superuser with the given details.
        Superusers have all permissions by default.
        
        Args:
            first_name (str): Superuser's first name
            last_name (str): Superuser's last name
            email (str): Superuser's email address
            username (str): Unique username
            password (str): Superuser's password
            
        Returns:
            Account: Created superuser instance
        """
        user = self.create_user(
            email       = self.normalize_email(email),
            username    = username,
            password    = password,
            first_name  = first_name,
            last_name   = last_name,
        )
        # Set superuser permissions
        user.is_admin        = True
        user.is_staff        = True
        user.is_active       = True
        user.is_superadmin   = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    """
    Custom user model that extends Django's AbstractBaseUser.
    Uses email as the unique identifier for authentication instead of username.
    
    Attributes:
        first_name (str): User's first name
        last_name (str): User's last name
        username (str): Unique username
        email (str): Unique email address
        phone_number (str): User's phone number
        date_joined (datetime): When the user account was created
        last_login (datetime): Last time the user logged in
        is_admin (bool): Admin status
        is_staff (bool): Staff status for admin site access
        is_active (bool): Whether this user account is active
        is_superadmin (bool): Superuser status
    """
    # Personal Information
    first_name      = models.CharField(max_length=50)
    last_name       = models.CharField(max_length=50)
    username        = models.CharField(max_length=50, unique=True)
    email           = models.EmailField(max_length=50, unique=True)
    phone_number    = models.CharField(max_length=50)

    # Account Status Fields
    date_joined     = models.DateTimeField(auto_now_add=True)
    last_login      = models.DateTimeField(auto_now_add=True)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    is_superadmin   = models.BooleanField(default=False)

    # Specify the fields used for authentication
    USERNAME_FIELD  = 'email'  # Use email as the unique identifier
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']
    
    # Assign the custom manager to objects
    objects = MyAccountManager()

    def __str__(self):
        """String representation of the user"""
        return self.email

    def has_perm(self, perm, obj=None):
        """Check if the user has a specific permission"""
        return self.is_admin

    def has_module_perms(self, add_label):
        """Check if the user has permissions to view the app `add_label`"""
        return True
