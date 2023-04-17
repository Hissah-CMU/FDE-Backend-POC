# pages/urls.py
from django.urls import path
from .views import generate_pdf

urlpatterns = [
    #path("", homePageView, name="home"),
    path('', generate_pdf, name='generate_pdf'),
]