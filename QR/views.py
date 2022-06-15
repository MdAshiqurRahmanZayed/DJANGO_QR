from django.conf import settings

# Create your views here.
from django.shortcuts import render

from pyzbar.pyzbar import decode
from PIL import Image

import pyqrcode


def qr_code(request):
   context = {}
   if request.method == 'POST':
       data = request.POST["data"]
       img = pyqrcode.create(data)
       file_name = "qr.png"
       context["qr_filename"] = file_name
       img.png(settings.MEDIA_ROOT + file_name, scale=10)
       
       
       
   return render(request, 'qr_code.html', context)


def index(request):
    return render(request, "index.html")


def qrcode_decoder(request):
   if request.method == "POST" and request.FILES['file']:
       context = {}
       qr_image = request.FILES['file']
       try:
                context['decoded'] = decode(Image.open(qr_image))[0].data.decode('ascii')   
       except:
           context['decoded'] = "It is not QR Image"
       return render(request, 'qr_upload.html', context)
   return render(request, 'qr_upload.html')