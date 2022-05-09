from django.urls import path

from . import views

urlpatterns = [
    path('datetime/', views.DatetimeView.as_view()), path('random/', views.RandomView.as_view()),
    ]
