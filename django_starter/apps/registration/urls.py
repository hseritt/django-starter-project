from django.urls import path
from django_starter.apps.registration.views import register, verify


urlpatterns = [
    path("register/", register, name="register"),
    path("verify/<uuid:verification>", verify, name="verify"),
]
