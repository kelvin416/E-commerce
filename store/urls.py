from unicodedata import name
from django.urls import path
from .views import store, checkout, cart

urlpatterns = [
    path('', store, name="store"),
    path('checkout/', checkout, name="checkout"),
    path('cart/', cart, name="cart"),
]
