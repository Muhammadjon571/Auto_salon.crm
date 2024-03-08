from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . import models
from . import serializers




@api_view(["GET"])
def employee_by_job(request):
    job = request.GET.get("job")
    job = models.Ishchi.objects.filter(job=job)
    ser = serializers.IshchiSerializers(job)
    return Response(ser.data)


@api_view(["GET"])
def employee_by_salary(request):
    salary = request.GET.get("salary")
    salary = models.Ishchi.objects.filter(salary=salary)
    ser = serializers.IshchiSerializers(salary)
    return Response(ser.data)

@api_view(["GET"])
def ishchi_by_tajriba(request):
    tajriba = request.GET.get("tajriba")
    tajriba = models.Ishchi.objects.filter(tajriba=tajriba)
    ser = serializers.IshchiSerializers(tajriba)
    return Response(ser.data)


@api_view(["GET"])
def ishchi_by_vaqti(request):
    vaqti = request.GET.get("vaqti")
    vaqti = models.Ishchi.objects.filter(vaqti=vaqti)
    ser = serializers.IshchiSerializers(vaqti)
    return Response(ser.data)


@api_view(["GET"])
def ishchi_by_manzili(request):
    manzili = request.GET.get("manzili")
    manzili = models.Ishchi.objects.filter(manzili__icontains=manzili)
    ser = serializers.IshchiSerializers(manzili)
    return Response(ser.data)


@api_view(["GET"])
def ishchi_by_yoshi(request):
    yoshi = request.GET.get("yoshi")
    yoshi = models.Ishchi.objects.filter(yoshi=yoshi)
    ser = serializers.IshchiSerializers(yoshi)
    return Response(ser.data)


@api_view(["GET"])
def buyurtma_by_telefon_raqam(request):
    telefon_raqam = request.GET.get("telefon_raqam")
    telefon_raqam = models.Buyurtma.objects.filter(telefon_raqam=telefon_raqam)
    ser = serializers.BuyurtmaSerializers(telefon_raqam)
    return Response(ser.data)


@api_view(["GET"])
def buyurtma_by_yetkazib_berish(request):
    yetkazib_berish = request.GET.get("yetkazib_berish")
    yetkazib_berish = models.Buyurtma.objects.filter(yetkazib_berish=yetkazib_berish)
    ser = serializers.BuyurtmaSerializers(yetkazib_berish)
    return Response(ser.data)




@api_view(["GET"])
def buyurtma_by_manzili(request):
    manzili = request.GET.get("manzili")
    manzili = models.Buyurtma.objects.filter(manzili=manzili)
    ser = serializers.BuyurtmaSerializers(manzili)
    return Response(ser.data)


@api_view(["GET"])
def tolov_by_kuni(request):
    kuni = request.GET.get("kuni")
    kuni = models.Tolov.objects.filter(kuni=kuni)
    ser = serializers.TolovSerializers(kuni)
    return Response(ser.data)


@api_view(["GET"])
def ijara_by_telefon(request):
    telefon = request.GET.get("telefon")
    telefon = models.Ijara.objects.filter(telefon=telefon)
    ser = serializers.IjaraSerializers(telefon)
    return Response(ser.data)

@api_view(["GET"])
def ijara_by_ism(request):
    ism = request.GET.get("ism")
    ism = models.Ijara.objects.filter(ism=ism)
    ser = serializers.IjaraSerializers(ism)
    return Response(ser.data)


@api_view(["GET"])
def ijara_by_olish_vaqti(request):
    olish_vaqti = request.GET.get("olish_vaqti")
    olish_vaqti = models.Ijara.objects.filter(olish_vaqti=olish_vaqti)
    ser = serializers.IjaraSerializers(olish_vaqti)
    return Response(ser.data)
