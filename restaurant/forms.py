from django import forms
from .models import Booking


# Code added for loading form data on the Booking page
class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        #fields = "__all__" # to include all fields of the Booking model but not recommended for production use
        fields = [
            'first_name', 'last_name', 'reservation_date', 
            'reservation_time', 'guest_number', 'seating_type', 'comment'
        ]

        # WIDGETS: Ini trik untuk mengubah tampilan input HTML
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'reservation_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'reservation_time': forms.TimeInput(attrs={'type': 'time', 'class': 'form-control'}),
            'guest_number': forms.NumberInput(attrs={'class': 'form-control', 'min': 1, 'max': 20}),
            'seating_type': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Allergies, birthday occasion, etc.'}),
        }
        
        # LABELS: Mengubah tulisan label agar lebih ramah
        labels = {
            'first_name': 'Nama Depan',
            'reservation_date': 'Tanggal Reservasi',
            'seating_type': 'Pilih Area Duduk',
        }