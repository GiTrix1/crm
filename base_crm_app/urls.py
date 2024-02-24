from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from .views import BaseView

app_name = "base_crm_app"

urlpatterns = [
    path("", BaseView.as_view(), name="base"),
    path(
        "login/",
        LoginView.as_view(
            template_name="registration/login.html",
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("accounts/logout/", LogoutView.as_view(), name="logout"),
]
