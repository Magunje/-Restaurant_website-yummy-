from typing import Self
from django import forms
from .models import Reservation


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['customer_name', 'customer_email','customer_phone','reservation_date', 'reservation_time', 'num_guests', 'table_number','message',]
        
        def __init__(self, *args, **kwargs):
                super().__init__(*args, **kwargs)
                
                self.fields['customer_name'].widget.attrs.update({'class': 'form-control', 'id': 'name', 'placeholder': 'Your Name'})
                self.fields['customer_email'].widget.attrs.update({'class': 'form-control', 'id': 'email', 'placeholder': 'Your Email'})
                self.fields['table_number'].widget.attrs.update({'class': 'form-control', 'id': 'table_number', 'placeholder': 'Table Number'})
                self.fields['reservation_date'].widget.attrs.update({'class':'date' 'form-control', 'id':'date', 'placeholder':'Date'})
                self.fields['reservation_time'].widget.attrs.update({'class': 'form-control', 'id': 'time', 'placeholder': 'Time'})
                self.fields['num_guests'].widget.attrs.update({'class': 'form-control', 'id': 'people', 'placeholder': 'Number Of People'})
                self.fields['customer_phone'].widget.attrs.update({'class': 'form-control', 'id': 'phone', 'placeholder': 'Your Phone'})
                self.fields['message'].widget.attrs.update({'class': 'form-control', 'rows': 5, 'placeholder': 'Message'})