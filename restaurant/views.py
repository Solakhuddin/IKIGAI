# from django.http import HttpResponse
from django.shortcuts import redirect, render, get_object_or_404

from .forms import BookingForm
from .models import Menu, Category, Booking, BookingItem



# Create your views here.
def home(request):
    return render(request, 'restaurant/index.html')

def about(request):
    return render(request, 'restaurant/about.html')

def book(request):
    form = BookingForm()
    # Kita butuh data menu untuk ditampilkan di form
    categories = Category.objects.prefetch_related('menu_items').all()

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            # 1. Simpan Data Booking Dulu (Header)
            booking_obj = form.save()
            
            # 2. Loop semua data yang dikirim user untuk mencari pesanan makanan
            for key, value in request.POST.items():
                if key.startswith('menu_') and value:
                    try:
                        menu_id = int(key.split('_')[1]) # Ambil ID dari string 'menu_5' -> '5'
                        qty = int(value)
                        
                        if qty > 0:
                            menu_obj = Menu.objects.get(id=menu_id)
                            # Simpan ke tabel BookingItem
                            BookingItem.objects.create(
                                reservation=booking_obj,
                                menu_item=menu_obj,
                                quantity=qty
                            )
                    except ValueError:
                        pass # Abaikan jika data error
            
            # Redirect ke halaman sukses/home
            return redirect('home') 

    context = {
        'form': form, 
        'categories': categories # Kirim menu ke template
    }
    return render(request, 'restaurant/book.html', context)

# Add your code here to create new views
def menu(request):
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