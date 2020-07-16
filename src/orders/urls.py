from django.conf.urls import url
from . import views

app_name = 'orders'

urlpatterns = [
    url(r'^create/$', views.order_create, name='order_create'),
    url(r'^process-payment/', views.process_payment, name='process_payment'),
    url(r'^payment_done/', views.payment_done, name='payment_done'),
    url(r'^payment_cancelled/', views.payment_cancel, name='payment_concelled'),

]