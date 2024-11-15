from django.db import models

# Create your models here.
class MenuType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Menu(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    menu_type = models.ForeignKey(MenuType, on_delete=models.CASCADE, related_name='menus')
    image =models.ImageField(upload_to = 'image/menu/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class GalleryImage(models.Model):
    image = models.ImageField(upload_to='image/gallery/')
    caption = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.caption or f"Gallery Image {self.id}"

class Event(models.Model):
    EventName = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    Description = models.TextField()
    Image = models.ImageField(upload_to='image/events/')

    def __str__(self):
        return self.EventName
    
class Chefs(models.Model):
    image = models.ImageField(upload_to='image/chiefs/')
    name = models.CharField(max_length=255)
    proffession = models.CharField(max_length=255)
    experience = models.TextField()

    def __str__(self):
        return self.name
    
class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    capacity = models.IntegerField()
    available = models.BooleanField(default='Available')
    
    def __str__(self):
        return f"{self.table_number} {self.available}"

class Reservation(models.Model):
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    num_guests = models.IntegerField()
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=20)
    table_number = models.ForeignKey(Table, on_delete=models.CASCADE)
    status = models.CharField(max_length=20, default='Pending')
    message = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.customer_name} {self.table_number}"