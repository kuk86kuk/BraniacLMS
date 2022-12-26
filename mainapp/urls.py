from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.HelloWordView.as_view()),
    path('', views.empty_str),
    path("<str:word>/", views.check_kwargs),
]