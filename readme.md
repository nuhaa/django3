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