from django.views import View
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Note


class NoteListCreateAPIView(APIView):
    def get(self, request: Request) -> Response:
        return Response(Note.objects.all())
