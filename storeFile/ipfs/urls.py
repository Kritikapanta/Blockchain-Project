from django.urls import path
from . import views

urlpatterns = [
    path('', views.uploadFile, name='uploadFile'),
    path('upload/', views.uploadToPinata, name='ipfs_upload'),
]
