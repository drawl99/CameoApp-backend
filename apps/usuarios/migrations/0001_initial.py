# Generated by Django 2.2 on 2020-03-05 04:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('talentos', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='EstadoCuenta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=15, verbose_name='Nombre')),
            ],
            options={
                'verbose_name': 'Estado Cuenta',
                'verbose_name_plural': 'Estado Cuentas',
                'ordering': ['nombre'],
            },
        ),
        migrations.CreateModel(
            name='UserClient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('biografia', models.CharField(blank=True, max_length=500, null=True)),
                ('avatar', models.CharField(blank=True, max_length=200, null=True)),
                ('user_twitter', models.CharField(blank=True, max_length=30, null=True)),
                ('estado', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='usuarios.EstadoCuenta')),
                ('favoritos', models.ManyToManyField(blank=True, to='talentos.Talent')),
                ('userClient', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
                'ordering': ['id'],
            },
        ),
    ]