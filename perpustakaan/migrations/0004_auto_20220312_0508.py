# Generated by Django 3.0.7 on 2022-03-12 05:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perpustakaan', '0003_auto_20220312_0449'),
    ]

    operations = [
        migrations.RenameField(
            model_name='buku',
            old_name='kelompok_id',
            new_name='kelompok',
        ),
    ]
