# Generated by Django 5.0 on 2023-12-07 10:25

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_profile'),
        ('modul_baca', '0006_alter_komentar_tgl_komentar'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='KomentarKreasi',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, max_digits=2)),
                ('tgl_komentar', models.DateTimeField(auto_now_add=True)),
                ('isi_komentar', models.TextField()),
                ('dari_buku', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='komentar', to='main.bukukreasi')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]