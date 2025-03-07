from django.urls import path
from .views import *

urlpatterns = [
    path('', BolimlarView.as_view(), name='bolimlar'),
    path('mahsulotlar/', MahsulotlarView.as_view(), name='mahsulotlar'),
    path('mijozlar/', MijozlarView.as_view(), name='mijozlar'),
    path('mahsulot_tahrirlash/<int:pk>/', MahsulotTahrirlshView.as_view(), name='mahsulot_tahrirlash'),
    path('mijoz_tahrirlash/<int:pk>/', MijozTahrirlashView.as_view(), name='mijoz_tahrirlash'),
    path('mahsulotlar/<int:pk>/delete/', mahsulot_delete_view, name='mahsulot_delete'),
    path('mijozlar/<int:pk>/delete/', mijoz_delete_view, name='mijoz_delete'),
    path('mahsulotlar/<int:pk>/dc/', mahsulot_dc_view, name='mahsulot_delete_confirm'),
    path('mijozlar/<int:pk>/dc/', mijoz_dc_view, name='mijoz_delete_confirm'),
]