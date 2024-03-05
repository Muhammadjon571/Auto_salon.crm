from django.shortcuts import render
from rest_framework.generics import ListAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, GenericAPIView
from main.models import *
from main.serializers import *



"----------START Ishchi CRUD----------"
class GetIshchi(ListAPIView):
    queryset = Ishchi.objects.all()
    serializer_class = IshchiSerializers


class CreateIshchi(ListCreateAPIView):
    queryset = Ishchi.objects.all()
    serializer_class = IshchiSerializers


class UpdateIshchi(UpdateAPIView):
    queryset = Ishchi.objects.all()
    serializer_class = IshchiSerializers


class DeleteIshchi(DestroyAPIView):
    queryset = Ishchi.objects.all()
    serializer_class = IshchiSerializers
"----------END Ishchi CRUD----------"


"----------START Buyurtma CRUD----------"
class GetBuyurtma(ListAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers


class CreateBuyurtma(ListCreateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers


class UpdateBuyurtma(UpdateAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers


class DeleteBuyurtma(DestroyAPIView):
    queryset = Buyurtma.objects.all()
    serializer_class = BuyurtmaSerializers
"----------END Buyurtma CRUD----------"


"----------START Kassa CRUD----------"

class GetKassa(ListAPIView):
    queryset = Kassa.objects.all()
    serializer_class = KassaSerializers


class CreateKassa(ListCreateAPIView):
    queryset = Kassa.objects.all()
    serializer_class = KassaSerializers

"----------END Kassa CRUD----------"


"----------START Tolov CRUD----------"
class GetTolov(ListAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializers


class CreateTolov(ListCreateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializers


class UpdateTolov(UpdateAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializers


class DeleteTolov(DestroyAPIView):
    queryset = Tolov.objects.all()
    serializer_class = TolovSerializers
"----------END Tolov CRUD----------"


"----------START Ijara CRUD----------"
class GetIjara(ListAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializers


class CreateIjara(ListCreateAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializers


class UpdateIjara(UpdateAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializers


class DeleteIjara(DestroyAPIView):
    queryset = Ijara.objects.all()
    serializer_class = IjaraSerializers
"----------END Ijara CRUD----------"


"----------START Davomat CRUD----------"
class GetDavomat(ListAPIView):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializers


class CreateDavomat(ListCreateAPIView):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializers


class UpdateDavomat(UpdateAPIView):
    queryset = Davomat.objects.all()
    serializer_class = DavomatSerializers


class DeleteDavomat(DestroyAPIView):
    queryset = Davomat.objects.all()
    serializer_class = IshchiSerializers
"----------END Davomat CRUD----------"