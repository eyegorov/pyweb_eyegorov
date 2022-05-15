from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


class LoginIndexView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, "login/templates/index.html")
