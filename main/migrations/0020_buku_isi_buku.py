# Generated by Django 4.1.3 on 2023-12-17 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_remove_buku_isi_buku'),
    ]

    operations = [
        migrations.AddField(
            model_name='buku',
            name='isi_buku',
            field=models.TextField(default='Sayangnya buku ini belum tersedia :(, silahkan coba buku lainnya'),
        ),
    ]