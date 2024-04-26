from django.contrib import admin
from .models import Page, Text
from mptt.admin import DraggableMPTTAdmin, TreeRelatedFieldListFilter


# Register your models here.
@admin.register(Page)  # регистрируем в админ.панели приложение Page
class PageAdmin(DraggableMPTTAdmin):  # создаем конфигурацию этого приложения в админке
	search_fields = ("name__startswith",)  # искать страницы можно по частичному совпадению названия
	list_display = ("tree_actions", "indented_title", "name", "url", "active",)  # какие поля отображаются в модели
	list_filter = ("active",)  # по каким полям делать сортировку в админке
	list_display_links = ("indented_title",)
	prepopulated_fields = {"url": ('name', )}  # url страницы пишется на основе названия страницы


@admin.register(Text)
class TextAdmin(admin.ModelAdmin):
	list_display = ("name", "title", "date_create", "date_update", "page_id",)
	list_filter = (
		("page_id", TreeRelatedFieldListFilter,),
	)
	list_editable = ("title",)  # добавляю возможность изменять title не заходя в сам текст в админ.панели



