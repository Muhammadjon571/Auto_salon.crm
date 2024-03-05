from rest_framework import serializers
from .models import *



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class IshchiSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ishchi
        fields = "__all__"



class BuyurtmaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = "__all__"



class KassaSerializers(serializers.ModelSerializer):
    class Meta:
        model = Kassa
        fields = "__all__"



class TolovSerializers(serializers.ModelSerializer):
    class Meta:
        model = Tolov
        fields = "__all__"



class IjaraSerializers(serializers.ModelSerializer):
    class Meta:
        model = Ijara
        fields = "__all__"



class DavomatSerializers(serializers.ModelSerializer):
    class Meta:
        model = Davomat
        fields = "__all__"