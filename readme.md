# run server
python3 manage.py runserver

# user password
username : admin
password : asd

# folder static
digunakan untuk menyimpan asset web, tambahkan deklarasi nya di setting.py code berikut

STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'static')
]

# untuk create administrator
python3 manage.py createsuperuser

# update module perpustakaan
- file /perpustakaan/admin.py
- tambahkan / import module (from perpustakaan.models import Buku, Kelompok)

# contoh queryset
- import model (books = Buku.objects.all())
- 

# form (perpustakaan/forms.py)
- import module form (from django.forms import ModelForm)

# widget (perpustakaan/forms.py bagian widgets)
- penambahan widget (class untuk form, ataupun penambahan id pada mode form)

