from unicodedata import name
from django.contrib import admin
from django.http import HttpRequest, HttpResponse
from django.urls import path
from perpustakaan.views import *
from django.contrib.auth.views import LoginView, LogoutView
# # untuk import satu per satu
# from perpustakaan.views import buku, penerbit, tambah_buku, ubah_buku

# untuk import lebih dari 1 module

urlpatterns = [
    path('admin/', admin.site.urls),
    path('buku/', buku, name='buku'),
    path('penerbit/', penerbit),
    path('tambah-buku/', tambah_buku, name='tambah_buku'),
    # path dengan penambahan name
    path('buku/ubah/<int:id_buku>', ubah_buku, name='ubah_buku'),
    path('buku/hapus/<int:id_buku>', hapus_buku, name='hapus_buku'),
    path('masuk/', LoginView.as_view(), name='masuk'),
    path('keluar/', LogoutView.as_view(next_page='masuk'), name='keluar'),
    path('signup/', signup, name='signup')
]
