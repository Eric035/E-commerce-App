from . import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.estore, name="estore"),
    path('checkout/', views.checkout, name="checkout"),
    path('cart/', views.cart, name="cart"),
] + static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)
