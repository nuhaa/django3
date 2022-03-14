from csv import excel
from django.forms import ModelForm, forms
from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm) :
    class Meta:
        model = Buku
        # # untuk menampilkan semua form
        # fields = '__all__'
        
        # # untuk menampilkan hanya form tertentu
        # fields = ['judul','penulis','kelompok']

        # untuk menampilkan exclude (selain)
        exclude = ['cover','tanggal']

        # widget forms
        widgets = {
            'judul' : forms.TextInput({'class':'form-control', 'placeholder':'Isikan Judul'}),
            'penulis' : forms.TextInput({'class':'form-control', 'placeholder':'Isikan Penulis'}),
            'penerbit' : forms.TextInput({'class':'form-control', 'placeholder':'Isikan Penerbit'}),
            'jumlah' : forms.NumberInput({'class':'form-control', 'placeholder':'Isikan Jumlah'}),
            'kelompok' : forms.Select({'class':'form-control', 'placeholder':'Isikan Kelompok'})
        }