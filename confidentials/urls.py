from django.urls import path

from .import views
urlpatterns = [
    path('',views.bank,name='confidentials-bank')
]
