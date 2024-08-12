from .models import Posts
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'anons', 'text', 'datetime']
        
        widgets = {
            'title': TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':"Название",
            }),
            'anons': TextInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':"Анонс",
            }),
            'text': Textarea(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':"Текст поста",
            }),
            'datetime': DateTimeInput(attrs={
                'class':'m-2 p-2 border-2 block',
                'placeholder':"дата и время",
                'type':'date'
            })
        }