from django.urls import path
from . import views

urlpatterns = [
    path('simple', views.simple, name="pokemao"),
    path('package', views.package, name="super_pokemao"),
]
