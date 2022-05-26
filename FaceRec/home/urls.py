from turtle import home
from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("contact",views.contact, name='contact'),
    path("emotion-detection/webcam/",views.webcam, name='webcam'),
    path("emotion-detection/", views.emotion_detection, name="emotion_detection"),
   path("emotion-detection/static-image/", views.emotion_detection_static_image, name="emotion_detection_start_image"),
    
]
