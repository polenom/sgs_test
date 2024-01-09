from django.urls import path

from login.views import UserLogin, CheckUser, UserRegistration, UserLogout, UserUpdate

app_name = "login"
urlpatterns = [
    path("", CheckUser.as_view()),
    path("login/", UserLogin.as_view(), name="login_user"),
    path("registration/", UserRegistration.as_view(), name="registration_user"),
    path("logout/", UserLogout.as_view(), name="logout_user"),
    path("update/", UserUpdate.as_view(), name="update_user")
]