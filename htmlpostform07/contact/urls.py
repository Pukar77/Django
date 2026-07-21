from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.contact_form, name="contact-form"),
    path('', views.submit_contact, name="submit_contact"),
]