from django.urls import path
from . import views

urlpatterns = [
    # ------------EMPLOYEE-----------------
    path('filter_employee_by_job/', views.employee_by_job),
    path('filter_employee_by_salary/', views.employee_by_salary),
    path('filter_ishchi_by_tajriba/', views.ishchi_by_tajriba),
    path('filter_ishchi_by_vaqti/', views.ishchi_by_vaqti),
    path('filter_ishchi_by_manzili/', views.ishchi_by_manzili),
    path('filter_ishchi_by_yoshi/', views.ishchi_by_yoshi),

    path('filter_buyurtma_by_yetkazib_berish/', views.buyurtma_by_yetkazib_berish),
    path('filter_buyurtma_by_telefon/', views.buyurtma_by_telefon_raqam),
    path('filter_buyurtma_by_manzili/', views.buyurtma_by_manzili),
    path('filter_tolov_by_kuni/', views.tolov_by_kuni),
    path('filter_ijara_by_telefon/', views.ijara_by_telefon),
    path('filter_ijara_by_ism/', views.ijara_by_ism),
    path('filter_ijara_by_olish_vaqti/', views.ijara_by_olish_vaqti),



]