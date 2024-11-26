from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login/", views.login_view, name="login-view"),
    path("login-user/", views.login_user, name="login-user"),
    path("logout-user/", views.logout_user, name="logout-user"),
    path("change-language/", views.change_language, name="change-language"),
    path("change-password-view/", views.change_password_view, name="change-password-view"),
    path("change-password/", views.change_password, name="change-password"),
    path("recover-password-view/", views.recover_password_view, name="recover-password-view"),
]
urlpatterns += staticfiles_urlpatterns()
