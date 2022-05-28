from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Note
from blog_api import serializers


class NoteListCreateAPIView(APIView):
    """ Представление, возвращает список объектов с помощью get """

    def get(self, request: Request):
        objects = Note.objects.all()
        serializer = serializers.NoteSerializer(
            instance=objects,
            many=True,
        )
        return Response(serializer.data)

    def post(self, request: Request):
        serializer = serializers.NoteSerializer(data=request.data)


class NoteDetailAPIView(APIView):
    """ Представление, возвращает уже существующий объект с помощью GET метода."""

    def get(self, request, pk):
        note = get_object_or_404(Note, pk=pk)
        serializer = serializers.NoteDetailSerializer(
            instance=note,
        )
        return Response(serializer.data)


class PublicNoteListAPIView(ListAPIView):
    queryset = Note.objects.all()
    serializer_class = serializers.NoteSerializer


def get_queryset(self):
    queryset = super().get_queryset()
    return queryset.filter(public=True)
