from django.contrib import admin
from .models import Booking, Menu, Category, BookingItem

# Register your models here.
# ihsan - admin404

class BookingItemInline(admin.TabularInline):
    model = BookingItem
    extra = 1 # Menampilkan 1 baris kosong untuk tambah manual

class BookingAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'reservation_date', 'seating_type', 'total_preorder_cost')
    inlines = [BookingItemInline] # Masukkan Inline ke sini

# admin.site.unregister(Booking)
admin.site.register(Booking, BookingAdmin)
admin.site.register(Menu)
admin.site.register(Category)
