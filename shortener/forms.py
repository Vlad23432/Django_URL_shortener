from django import forms
from .models import Links


class CreateUrlForm(forms.ModelForm):
	name = forms.CharField(
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'название ссылки'}
		))
	original_url = forms.CharField(
		widget=forms.TextInput(
			attrs={'class': 'form-control', 'placeholder': 'вставьте линную ссылку'}))

	# формами ModelForm легче управлять при создании новых объектов БД
	class Meta:
		model = Links
		fields = ["name", "original_url",]  # указываю поля, которые должны будут отображаться в форме
		# exclude = ["user", "short_url", "clicks_qty", "created_at",]
		# fields = "__all__" <- оставить ВСЕ поля модели для отображения в форме






