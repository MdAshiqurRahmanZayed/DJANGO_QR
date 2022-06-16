from django.apps import AppConfig
from pyzbar.pyzbar import decode

class QrConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'QR'
