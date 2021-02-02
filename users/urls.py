
from django.conf.urls import url
from users.views import dashboard, register, validate_username
from django.urls import path, include

urlpatterns = [
    url(r"^dashboard/", dashboard, name="dashboard"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^register/", register, name="register"),
    url(r'^ajax/validate_username/$', validate_username, name='validate_username'),
]