from django.shortcuts import render
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
# from django.http import HttpRequest, HttpResponse

# Create your views here.
def buku(request):
    # return HttpResponse('Halaman Buku')
    # judul = ["Belajar Django","Belajar Python","Belajar Apapun"]
    books = Buku.objects.all()
    konteks = {
        'books':books
    }
    return render(request,'buku.html', konteks)

def penerbit(request):
    # return HttpResponse('<h1>Halaman Penerbit</h1>')
    return render(request, 'penerbit.html')

def tambah_buku(request) :
    form = FormBuku()

    konteks = {
        'form' : form,
    }

    return render(request, 'tambah-buku.html', konteks)