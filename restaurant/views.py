# from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .forms import BookingForm
from .models import Menu, Category



# Create your views here.
def home(request):
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def book(request):
    form = BookingForm()
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form':form}
    return render(request, 'restaurant/book.html', context) 

# Add your code here to create new views
def menu(request):
    # Ambil semua kategori
    # (Optional) prefetch_related digunakan agar query database lebih ringan/cepat
    categories = Category.objects.prefetch_related('menu_items').all()
    
    context = {'categories': categories}
    return render(request, 'restaurant/menu.html', context)

def menu_detail(request, pk=None):
    if pk is None:
        return render(request, 'restaurant/menu_detail.html', {'menu': 'Sorry no menu item found!'})
    # menu = Menu.objects.get(pk=pk) # can crash if pk not found
    menu_item = get_object_or_404(Menu, pk=pk)
    return render(request, 'restaurant/menu_detail.html', {'menu': menu_item})