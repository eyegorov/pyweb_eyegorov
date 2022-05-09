from django.http import HttpRequest, HttpResponse
from django.shortcuts import render  # команда render берет шаблон и
# выводит HttpResponse
from django.views import View


class PrintView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return HttpResponse("""<h1>Hello, World</h1>""")

class IndexView(View):
    def get(self, request):
        return render(request, "common/index.html")