from django.contrib import admin
from .models import Note


@admin.register(Note)  # связываем админку с моделью
class NoteAdmin(admin.ModelAdmin):
    # Поля в списке
    list_display = ('title', 'id', 'public', 'update_at', 'author', )
    # #
    # # # Группировка поля в режиме редактирования
    fields = (('title', 'public'), 'message', 'author', 'create_at', 'update_at')
    # Поля только для чтения в режиме редактирования
    readonly_fields = ('create_at', 'update_at')
    # #
    # Поиск по выбранным полям
    search_fields = ['title']
    #
    # Фильтры справа
    list_filter = ('public', 'author', )
