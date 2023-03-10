# Generated by Django 4.1.5 on 2023-01-23 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('idCategoria', models.IntegerField(primary_key=True, serialize=False, verbose_name='Id de Categoria')),
                ('nombreCategoria', models.CharField(max_length=30, verbose_name='Nombre de Categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Gato',
            fields=[
                ('chip', models.CharField(max_length=6, primary_key=True, serialize=False, verbose_name='Chip')),
                ('nombre', models.CharField(max_length=20, verbose_name='Nombre')),
                ('raza', models.CharField(max_length=20, verbose_name='Raza')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.categoria')),
            ],
        ),
    ]
