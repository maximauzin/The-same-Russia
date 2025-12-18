from django import forms
from .models import News, TeamMember, Partner, HistoryLine, NewsImage

class NewsForm(forms.ModelForm):
    photos = forms.FileField(
        label='Добавить фотографии в галерею',
        required=False
    )

    class Meta:
        model = News
        fields = ['title', 'short_description', 'main_content', 'image', 'display_style'] # Обновлены поля
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Название новости'}),
            'short_description': forms.Textarea(attrs={'placeholder': 'Краткое описание (для списков)', 'rows': 3}),
            'main_content': forms.Textarea(attrs={'placeholder': 'Основной текст новости', 'id': 'news-content'}),
            'image': forms.ClearableFileInput(),
            'display_style': forms.RadioSelect(attrs={'class': 'display-style-radio'}),
        }

class TeamMemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['last_name', 'first_name', 'middle_name', 'role', 'position', 'vk_link', 'photo']
        widgets = {
            'last_name': forms.TextInput(attrs={'id': 'second-name'}),
            'first_name': forms.TextInput(attrs={'id': 'first-name'}),
            'middle_name': forms.TextInput(attrs={'id': 'third-name'}),
            'role': forms.TextInput(attrs={'id': 'royle'}),
            'position': forms.TextInput(attrs={'id': 'post'}),
            'vk_link': forms.TextInput(attrs={'id': 'reference'}),
            'photo': forms.FileInput(attrs={'id': 'image'}),
        }

class PartnerForm(forms.ModelForm):
    class Meta:
        model = Partner
        fields = ['name', 'logo', 'url']

class HistoryLineForm(forms.ModelForm):
    class Meta:
        model = HistoryLine
        fields = ['title', 'description', 'years', 'location', 'image']