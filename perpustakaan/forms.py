from csv import excel
from django.forms import ModelForm, forms
from django.forms import ModelForm
from django import forms
from perpustakaan.models import Buku

class FormBuku(ModelForm) :
    class Meta:
        model = Buku
        ## untuk menampilkan semua form
        # fields = '__all__'
        
        # # untuk menampilkan hanya form tertentu
        # fields = ['judul','penulis','kelompok']

        # untuk menampilkan exclude (selain)
        exclude = ['penerbit']

        # widget forms
        widgets = {
            'judul' : forms.TextInput({'class':'form-control'}),
            'penulis' : forms.TextInput({'class':'form-control'}),
            'jumlah' : forms.NumberInput({'class':'form-control'}),
            'kelompok' : forms.Select({'class':'form-control'})
        }