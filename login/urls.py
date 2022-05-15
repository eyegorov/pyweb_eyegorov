from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views  # "." означает текущее приложение, на случай, если приложение будет переименовано и тп.

urlpatterns = [
    path('login/', views.LoginIndexView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)