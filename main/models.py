from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator, EmailValidator
from .validators import ImageFileValidator
from django.core.exceptions import ValidationError
from django.core.validators import FileExtensionValidator


class User(AbstractUser):
    telefon_raqami = models.CharField(max_length=13, verbose_name='telefon raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    bio = models.CharField(max_length=255)

    class Meta(AbstractUser.Meta):
        swappable = 'AUTH_USER_MODEL'
        verbose_name = 'User'
        verbose_name_plural = 'Users'


class Ishchi(models.Model):
    user = models.ForeignKey(to='User', verbose_name='foydalanuvchi', on_delete=models.CASCADE)
    yoshi = models.IntegerField(default=18)
    manzili = models.CharField(default=False)
    LAVOZIM_CHOICES = (
        ('director', 'director'),
        ('manager', 'manager'),
        ('sotuvchi', 'sotuvchi'),
    )
    lavozim = models.CharField(max_length=25, verbose_name='lavozimi', choices=LAVOZIM_CHOICES)
    ish_tajribasi = models.CharField(max_length=255, verbose_name='ish_staji')
    ish_vaqti = models.TimeField()
    oylik = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='oylik')

    def __str__(self):
        return self.oylik


class Buyurtma(models.Model):
    buyurtmachi_ismi = models.CharField(max_length=55, verbose_name='mijoz_ismi')
    telefon_raqami = models.CharField(max_length=13, verbose_name='telefon raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    is_delivery = models.BooleanField(default=False, verbose_name='yetkazilga va yetkazilmaganligi')
    yetkazib_berish_kuni = models.DateTimeField()
    manzil = models.CharField(max_length=255, verbose_name='manzil')
    RUSUMI_CHOICES = (
        ('Malibu', 'Malibu')
        ('Cobalt', 'Cobalt')
        ('Gentra', 'Gentra')
        ('Nexia 3', 'Nexia 3')
        ('Tahoe', 'Tahoe')
        ('Traverse', 'Traverse')
        ('Tracker 2', 'Tracker 2')
        ('Damas', 'Damas')
    )
    mashina_rusumi = models.CharField(max_length=25, verbose_name='mashina rusumi', choices=RUSUMI_CHOICES)
    RANGI_CHOICES = (
        ('Oq', 'Oq')
        ('Qora', 'Qora')
        ('Qizil', 'Qizil')
        ('Kulirang', 'Kulirang')
    )
    mashina_rangi = models.CharField(max_length=25, verbose_name='mashina_rangi', choices=RANGI_CHOICES)
    narxi = models.DecimalField(max_length=20, decimal_places=2, verbose_name='narxi')

    def __str__(self):
        return self.buyurtmachi_ismi


class Kassa(models.Model):
    summa = models.DecimalField(max_digits=20, decimal_places=2, verbose_name='tolov_summasi')

    def __str__(self):
        return self.summa


class Tolov(models.Model):
    buyurtma = models.ForeignKey(to='Buyurtma', on_delete=models.CASCADE)
    tolov_summasi = models.DecimalField(max_length=20, verbose_name='tolov_miqdori', decimal_places=2)
    kuni = models.DateTimeField(auto_now=True, verbose_name='tolov_kuni')

    def __str__(self):
        return self.buyurtma


class Ijara(models.Model):
    ijarachi_ismi = models.CharField(max_length=55, verbose_name='Ijarachi_ismi')
    telefon_raqami = models.CharField(max_length=13, verbose_name='telefon raqam', unique=True, validators=[
        RegexValidator(
            regex='^[\+]9{2}8{1}[0-9]{9}$',
            message='Invalid phone number',
            code='invalid_number'
        ), ])
    pasport_seria_raqami = models.CharField(max_length=255, verbose_name='seria_raqami')
    MASHINA_CHOICES = (
        ('Malibu', 'Malibu')
        ('Nexia 3', 'Nexia 3')
        ('Cobalt', 'Cobalt')
        ('Gentra', 'Gentra')
        ('Spark', 'Spark')
    )
    mashina_rusumi = models.CharField(max_length=25, verbose_name='mashina_rusumi', choices=MASHINA_CHOICES)
    mashina_raqami = models.CharField(max_length=25, verbose_name='mashina_raqami')
    olish_vaqti = models.DateTimeField(verbose_name='olish_vaqti')
    qaytarish_vaqti = models.DateTimeField(verbose_name='qaytarish_vaqti')
    narxi = models.DecimalField(max_length=10, decimal_places=2, verbose_name='narxi')

    def __str__(self):
        return self.ijarachi_ismi


class Davomat(models.Model):
    ishchi = models.ForeignKey(to='Employee', verbose_name='ishchi', on_delete=models.CASCADE)
    kun = models.DateTimeField(auto_now=True, verbose_name='sana')
    davomat = models.BooleanField(default=False, verbose_name='Davomat')