from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path("contact.html", views.contact, name = "contact"),
    path("about.html", views.about, name = "about"),
    path("products.html", views.products, name = "products"),
    path("about.html", views.activity, name = "activity"),

]