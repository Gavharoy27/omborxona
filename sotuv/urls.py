from django.urls import path
from .views import *

urlpatterns = [
    path('', SotuvlarView.as_view(), name='sotuvlar'),
    path('sotuv_tahrirlash/<int:pk>/', SotuvTahrirlashView.as_view(), name='sotuv_tahrirlash'),
    path('<int:pk>/delete/', sotuv_delete_view, name='sotuv_delete'),
    path('<int:pk>/dc/', sotuv_dc_view, name='sotuv_delete_confirm'),
    path('ogohlantirish/', ogohlantirish_view, name='ogohlantirish')
]