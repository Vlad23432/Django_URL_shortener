from django.shortcuts import render
from .models import Page


# Create your views here.
def page_view(request, url):
	page = Page.objects.get(url=url)  # из базы данных достать объект страницы, где поле url совпадает с запрошенным url
	return render(request, 'content/page.html', {'page': page})
