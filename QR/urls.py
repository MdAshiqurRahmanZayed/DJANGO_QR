from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name="home"),
    path('qr-code', views.qr_code, name='qr_code'),
    path('qr-code-decoder', views.qrcode_decoder, name='qrcode_decoder')
]
