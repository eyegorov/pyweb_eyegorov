from datetime import datetime
from random import random

from django.http import HttpRequest, HttpResponse
from django.views import View


class DatetimeView(View):
    def get(self, request: HttpRequest) -> HttpResponse:  # Request всегда должен возвращать какой-либо запрос
        now = datetime.now()

        return HttpResponse(now)


class RandomView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        random_number = random()

        return HttpResponse(random_number)
