from django.shortcuts import render, redirect
from django.urls import reverse
from .models import MenuType, Menu, GalleryImage, Event,Chefs,Reservation
from .forms import ReservationForm

# Create your views here.
def home(request):
    menu_types = MenuType.objects.all()
    menus = Menu.objects.all()
    gallery = GalleryImage.objects.all()
    events = Event.objects.all()
    chef = Chefs.objects.all()
    
    context = {
        'menu_types': menu_types,
        'menus': menus,
        'gallery' : gallery,
        'events' : events,
        'chef' :chef,
    }
    return render(request, 'index.html', context)

def book (request):
    if request.method == 'POST':
        reservation_form = ReservationForm(request.POST)
        if reservation_form.is_valid():
            reservation_form.save()
            return redirect(reverse('home'))
    else:
        reservation_form = ReservationForm()
    context = {
        'reservation_form' : reservation_form
    }
    return render (request, 'base.html', context)