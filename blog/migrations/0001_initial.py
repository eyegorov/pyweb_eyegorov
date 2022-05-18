# Generated by Django 4.0.4 on 2022-05-18 06:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, verbose_name='Заголовок')),
                ('message', models.TextField(max_length=10000, verbose_name='Текст статьи')),
                ('public', models.BooleanField(default=False, verbose_name='Опубликовать')),
                ('create_at', models.DateField(auto_now=True, verbose_name='Время создания')),
                ('update_at', models.DateField(auto_now_add=True, verbose_name='Время обновления')),
                ('author_at', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
