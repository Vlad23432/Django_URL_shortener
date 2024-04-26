from django.shortcuts import render
from .models import Page


# Create your views here.
def page_view(request, url, child_url=None):
	try:
		page = Page.objects.get(url=child_url)  # из базы данных достать объект страницы, где поле url совпадает с запрошенным url
	except:
		page = Page.objects.get(url=url)
	return render(request, 'content/page.html', {'page': page})
