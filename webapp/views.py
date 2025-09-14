from django.shortcuts import render
from django.http import FileResponse
import os
from django.conf import settings

# Create your views here.

def Index(request):
    return render(request,"Index.html")

def download_resume(request):
    filepath = os.path.join(settings.BASE_DIR, 'webapp/static/files/Surya_CV.pdf')
    return FileResponse(open(filepath, 'rb'), as_attachment=True, filename='Surya_CV.pdf')