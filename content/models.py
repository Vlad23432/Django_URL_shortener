from django.db import models


# Create your models here.
class Page(models.Model):  # CREATE TABLE 'page'
	name = models.CharField('Название страницы', max_length=100, db_index=True)
	url = models.SlugField('URL страницы', max_length=255, db_index=True, unique=True)
	active = models.BooleanField('Отображать в меню?', default=True)

	class Meta:
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'

	def __str__(self):
		return self.name

