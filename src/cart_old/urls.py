from django.urls import path, include

from .views import ListCart

# Cart Urls

app_name = 'cart'

urlpatterns = [
    path('', ListCart.as_view(), name='list-carts')
]