from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="index-home"),
    path('login/',views.login_view, name="login"),
    path('register/',views.register, name="register"),
    path('map/',views.map, name="maps"),
    path('vehicle-info/',views.veh_info, name="vehicle-info"),
    path('behaviour-analysis/',views.beh_analysis, name="behaviour-analysis"),
    path('profile/',views.profile, name="profile"),
    path('drive-storage/',views.drive, name="drive"),
    path('about/',views.about, name="about"),
    path('services/',views.services, name="services"),
    path('gallery/',views.gallery, name="gallery"),
    path('contact/',views.contact, name="contact"),
    path('terms/',views.terms, name="terms"),
]