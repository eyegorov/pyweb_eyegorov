from rest_framework import serializers

from blog.models import Note, Comment


class NoteSerializer(serializers.ModelSerializer):
    class Meta:  # Класс, описывающий конфигурацию
        model = Note  # Базовая модель, на которую опирается
        fields = "__all__" # Поля,которые буду выводиться
        read_only = "author_at"  # Поля,которые не будут выводиться


class CommentSerializer(serializers.ModelSerializer):
    rating = serializers.SerializerMethodField('get_rating')

    def get_rating(self, obj: Comment):
        return {
            'value': obj.rating,
            'display': obj.get_rating_display()
        }

    class Meta:
        model = Comment
        fields = "__all__"


class NoteDetailSerializer(serializers.ModelSerializer):
    """ Одна статья блога """
    author = serializers.SlugRelatedField(
        slug_field="email",  # указываем новое поле для отображения
        read_only=True  # поле для чтения
    )
    comments = CommentSerializer(many=True, read_only=True)  # one-to-many-relationships

    class Meta:
        model = Note
        fields = (
            'title', 'message', 'create_at', 'update_at', 'public',  # из модели
            'author_at', 'comments',  # данные из models.py, заголовки атрибуты (поля) должны быть идентичны
        )
