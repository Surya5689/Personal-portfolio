from django.urls import path
from webapp import views

urlpatterns=[
    path('',views.Index,name="Index"),
    path('download-resume/', views.download_resume, name="download_resume"),
]