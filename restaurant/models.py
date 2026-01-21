# file models.py
from django.db import models

# Create your models here.
class Booking(models.Model):
   SEATING_CHOICES = [
        ('counter', 'Omakase Counter (Depan Chef)'),
        ('private', 'Private Tatami Room'),
        ('table', 'Regular Table'),
   ]
   first_name = models.CharField(max_length=200)    
   last_name = models.CharField(max_length=200)
   reservation_date = models.DateField(null=True)
   reservation_time = models.TimeField(null=True)
   guest_number = models.PositiveIntegerField()
   # Field for table seating type with choices
   seating_type = models.CharField(
        max_length=20, 
        choices=SEATING_CHOICES, 
        default='table'
   )
   comment = models.TextField(blank=True, null=True, max_length=500)

   def __str__(self):
      return f"{self.first_name} - {self.seating_type} ({self.reservation_date})"


# Add code to create Menu model
# Model 1: Kategori (Misal: Appetizer, Main Course, Dessert)
class Category(models.Model):
   name = models.CharField(max_length=100)
    
   class Meta:
      verbose_name_plural = "Categories" # Agar di Admin panel tulisannya benar

   def __str__(self):
      return self.name

# Model 2: Item Makanan
class Menu(models.Model):
   name = models.CharField(max_length=200)
   description = models.TextField(blank=True)
   price = models.DecimalField(max_digits=10, decimal_places=2) # Pakai Decimal utk uang
   image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    
   # RELASI: Satu menu punya satu kategori
   category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="menu_items", null=True)
    
   # Label Diet
   is_spicy = models.BooleanField(default=False)
   is_available = models.BooleanField(default=True) # Untuk hide menu kalau sold out

   def __str__(self):
      return self.name