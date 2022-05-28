from django.shortcuts import get_object_or_404
from rest_framework.generics import ListAPIView
# from rest_framework.permissions import IsAuthenticatedOrReadOnly
# но разрешить доступ только для чтения для неаутентифицированных пользователей
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from blog.models import Note
from blog_api import serializers


class NoteListCreateAPIView(APIView):
    # permission_classes = IsAuthenticatedOrReadOnly
    # простой стиль разрешения - разрешить доступ любому
    # аутентифицированному пользователю и запретить доступ любому неаутентифицированному пользователю.
    # Это соответствует классу IsAuthenticated в REST framework.
    # IsAuthenticatedOrReadOnly - разрешить полный доступ для аутентифицированных пользователей,
    # но разрешить доступ только для чтения для неаутентифицированных пользователей

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
        author = request.user
        serializer.save(author=author)  # способ передачи дополнительных данных через метод save
    # то есть таким способом можно добавить данные, которые уже лежат в сериализаторе


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

    def get_queryset(self):  # Любые обработки с данными queryset лучше делать в отдельном методе
        queryset = super().get_queryset()
        return queryset.filter(public=True)  # отфильтровывать только публичные записи (author_at=self.request.user)

    def filter_queryset(self, queryset):
        ...
