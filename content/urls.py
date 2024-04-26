from django.urls import path
from . import views


urlpatterns = [
	path('<slug:url>/', views.page_view, name='page_detail'),  # путь генерируется автоматически полем url из модели Page
	path('<slug:url>/<slug:child_url>/', views.page_view, name='page_nested'),
]

