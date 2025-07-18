from django.urls import path
from main.views import home,login,register
urlpatterns=[
    path("",home,name="home"),
    path("login/",login,name="Login"),
    path("register/",register,name="Register")
]