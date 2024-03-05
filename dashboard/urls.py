from django.urls import path
from .views import *


urlpatterns = [
    #---------------START Ishchi URL---------------#
    path('get-ischi/', GetIshchi.as_view()),
    path('create-ischi/', CreateIshchi.as_view()),
    path('update-ischi/', UpdateIshchi.as_view()),
    path('delete-ischi/', DeleteIshchi.as_view()),
    #---------------START Buyurtma URL---------------#
    path('get-buyurtma/', GetBuyurtma.as_view()),
    path('create-buyurtma/', CreateBuyurtma.as_view()),
    path('update-buyurtma/', UpdateBuyurtma.as_view()),
    path('delete-buyurtma/', DeleteBuyurtma.as_view()),
    #---------------START Tolov URL---------------#
    path('get-tolov/', GetTolov.as_view()),
    path('create-tolov/', CreateTolov.as_view()),
    path('update-tolov/', UpdateTolov.as_view()),
    path('delete-tolov/', DeleteTolov.as_view()),
    #---------------START Ijara URL---------------#
    path('get-ijara/', GetIjara.as_view()),
    path('create-ijara/', CreateIjara.as_view()),
    path('update-ijara/', UpdateIjara.as_view()),
    path('delete-ijara/', DeleteIjara.as_view()),
    #---------------START Davomat URL---------------#
    path('get-davomat/', GetDavomat.as_view()),
    path('create-davomat/', CreateDavomat.as_view()),
    path('update-davomat/', UpdateDavomat.as_view()),
    path('delete-davomat/', DeleteDavomat.as_view()),
    #---------------START Kassa URL---------------#
    path('get-kassa/', GetKassa.as_view()),
    path('create-kassa/', CreateKassaKassa.as_view()),
]