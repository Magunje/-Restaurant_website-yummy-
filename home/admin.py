from django.contrib import admin
from . models import Menu,MenuType,GalleryImage,Event,Chefs,Table,Reservation

# Register your models here.
@admin.register(Reservation) 
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'table_number', 'num_guests', 'message', 'reservation_date']

    
@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ['table_number', 'capacity', 'available']
 
 
@admin.register(MenuType)
class MenuTypeAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    
@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'menu_type', 'price', 'created_at']

    
@admin.register(GalleryImage)
class GalleryAdmin(admin.ModelAdmin):
    list_display = ['caption', 'created_at']
    
    
@admin.register(Chefs)
class ChefsAdmin(admin.ModelAdmin):
    list_display = ['name', 'proffession', 'experience']
    
    
@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['EventName', 'Description', 'price']