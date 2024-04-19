from django.db import models
from mptt.models import MPTTModel, TreeForeignKey


# Create your models here.
class Page(MPTTModel):  # CREATE TABLE 'page'
	name = models.CharField('Название страницы', max_length=100, db_index=True)
	url = models.SlugField('URL страницы', max_length=255, db_index=True, unique=True)
	active = models.BooleanField('Отображать в меню?', default=True)
	parent = TreeForeignKey('self', blank=True, null=True, db_index=True,
	                        on_delete=models.CASCADE, default=None)

	class Meta:
		verbose_name = 'Страница'
		verbose_name_plural = 'Страницы'
		ordering = ('tree_id', 'level')

	def __str__(self):
		return self.name

