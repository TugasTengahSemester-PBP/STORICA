# Generated by Django 4.2.6 on 2023-10-26 04:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0008_alter_buku_tanggal_terbit'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buku',
            name='tanggal_terbit',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='buku',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]