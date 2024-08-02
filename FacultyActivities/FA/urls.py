from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('admin',views.admin),
    path('admin_login',views.admin_login),
    path('details',views.admin_dashboard),
    path('faculty',views.fac_login),
    path('fac_login',views.fac_login),
    path('entry',views.fac_dashboard),
    path('enter_detail',views.detail_enter,name="table_enter"),
    path('submit_details',views.detail_enter),
    path('goback_facdash',views.goback_facdash),
    path('handle_filters',views.handle_filters),
    path('it_detail_enter',views.it_detail_enter),
    path('it_submit_details',views.it_detail_enter),
    path('it_handle_filters',views.it_handle_filters),
    path('so_submit_details',views.so_detail_enter),
    path('so_handle_filters',views.so_handle_filters),
    path('so_detail_enter',views.so_detail_enter)
]