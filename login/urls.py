from django.urls import path

from . import views  # "." означает текущее приложение, на случай, если приложение будет переименовано и тп.

urlpatterns = [
    path('login/', views.LoginIndexView.as_view()),
]