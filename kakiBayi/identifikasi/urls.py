from django.urls import path
from identifikasi import views

urlpatterns = [
    path('',views.index, name="index"),
    path('pelatihan',views.pelatihan, name="pelatihan"),
    path('identifikasi',views.pengujian, name="pengujian"),
]