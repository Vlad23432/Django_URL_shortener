from django.contrib import admin
from .models import Page


# Register your models here.
@admin.register(Page)  # регистрируем в админ.панели приложение Page
class PageAdmin(admin.ModelAdmin):  # создаем конфигурацию этого приложения в админке
	search_fields = ("name__startswith",)  # искать страницы можно по частичному совпадению названия
	list_display = ("name", "url", "active",)  # какие поля отображаются в модели
	list_filter = ("active",)  # по каким полям делать сортировку в админке


