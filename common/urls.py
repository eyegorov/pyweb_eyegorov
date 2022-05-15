from django.urls import path
from django.contrib import admin


from . import views  # "." означает текущее приложение, на случай, если приложение будет переименовано и тп.

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', views.PrintView.as_view()),
    path('', views.IndexView.as_view()),
    ]

