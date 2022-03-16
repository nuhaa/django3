from django.shortcuts import render, redirect
from perpustakaan.models import Buku
from perpustakaan.forms import FormBuku
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.conf import settings
# from django.http import HttpRequest, HttpResponse

def hapus_buku(request,id_buku):
    buku = Buku.objects.filter(id=id_buku)
    buku.delete()
    messages.success(request, "Data Berhasil Di Hapus")
    return redirect('buku')


def ubah_buku(request, id_buku):
    buku = Buku.objects.get(id=id_buku)
    template = 'ubah-buku.html'
    if request.POST:
        form = FormBuku(request.POST,instance=buku)
        if form.is_valid():
            form.save()
            messages.success(request, "Data Berhasil Di Perbaharui")
            return redirect('ubah_buku', id_buku=id_buku)
    else :
        form = FormBuku(instance=buku)
        konteks = {
            'form':form,
            'buku':buku
        }
        return render(request, template, konteks)

# Create your views here.
@login_required(login_url=settings.LOGIN_URL)
def buku(request):
    # return HttpResponse('Halaman Buku')
    # judul = ["Belajar Django","Belajar Python","Belajar Apapun"]
    
    # get all
    books = Buku.objects.all()
    
    # # get filter jumlah
    # books = Buku.objects.filter(kelompok_id=1)
    
    # # get filter kelompok id (foreign key with nama foreign key)
    # books = Buku.objects.filter(kelompok_id__nama='Novel')
    
    # # get filter kelompok id (foreign key with nama foreign key) dengan penambahan limit
    # books = Buku.objects.filter(kelompok_id__nama='Produktif')[:2]
    konteks = {
        'books':books
    }
    return render(request,'buku.html', konteks)

def penerbit(request):
    # return HttpResponse('<h1>Halaman Penerbit</h1>')
    return render(request, 'penerbit.html')

def tambah_buku(request) :
    # konteks data yang akan di lempar ke tampilan
    form = FormBuku()
    konteks = {
        'form': form,
    }
    # jika ada request method post
    if request.POST:
        # form request POST
        form = FormBuku(request.POST, request.FILES)
        # jika form nya valide
        if form.is_valid():
            # form akan di save
            form.save()
            konteks.update({'pesan': "Data Berhasil Disimpan"})
            return render(request, 'tambah-buku.html', konteks)

    return render(request, 'tambah-buku.html', konteks)
