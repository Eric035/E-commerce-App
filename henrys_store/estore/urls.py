from . import views
from django.urls import path

urlpatterns = [
    path('', views.estore, name="estore"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
]
