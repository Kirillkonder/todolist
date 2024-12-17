from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser, Todo

from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class UserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUser
        fields = ('username', 'nickname', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Убираем метки и подсказки
        for field_name, field in self.fields.items():
            field.label = ''
            field.help_text = None
            
            # Устанавливаем плейсхолдеры
            placeholders = {
                'username': 'Имя пользователя',
                'nickname': 'Псевдоним',
                'password1': 'Пароль',
                'password2': 'Повторите пароль'
            }
            field.widget.attrs['placeholder'] = placeholders.get(field_name, '')  # Плейсхолдеры для каждого поля
            
            # Добавляем классы для стилизации и отступов
            field.widget.attrs['class'] = 'form-control rounded-pill mb-3'  # Класс для отступов (например, mb-3 для нижнего отступа)




class LoginForm(forms.Form):
    username = forms.CharField(label='Имя пользователя', max_length=100)
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput())


class TodoForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ['title']
        labels = {'title': ''}  # Убираем заголовок поля
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control custom-title',  # Добавляем класс для стилизации
                'placeholder': 'Введите название задачи'  # Плейсхолдер
            }),
        }