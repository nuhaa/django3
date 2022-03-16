Link Youtube
https://www.youtube.com/playlist?list=PLSCLBARdXrOz4SM3GKyKuqQp7eXWAH1u1

Konsep Django MVT
- Model (database)
- View (Kontrol, berisi fungsi2 mengatur http request dan response)
- Template (User interface, berisi berkas2 HTML)

# run server
python3 manage.py runserver

# user administrator
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

# form (perpustakaan/forms.py)
- import module form (from django.forms import ModelForm)

# widget (perpustakaan/forms.py bagian widgets)
- penambahan widget (class untuk form, ataupun penambahan id pada mode form)

# penambahan flash message
- import module message pada file 'perpustakaan/views.py' from django.contrib import messages

# upload file
- setting perpus/settings.py
- tambahkan 
    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR,'media')
- untuk bisa di akses tambahkan juga
    TEMPLATES => OPTION => context_processors
        'django.template.context_processors.media',
- install pillow (package untuk upload media, pip install pillow)

# login
- import module di file "urls.py" from "django.contrib.auth.views import login_required"
- 