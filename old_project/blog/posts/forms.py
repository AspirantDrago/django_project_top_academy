from .models import Posts
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea, ClearableFileInput


class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['title', 'anons', 'text', 'image', 'datetime']
        
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
                'rows':4,
                
            }),
            'image':ClearableFileInput(attrs={
                'class':"relative m-0 block w-full min-w-0 flex-auto cursor-pointer rounded border border-solid border-secondary-500 bg-transparent bg-clip-padding px-3 py-[0.32rem] text-base font-normal text-surface transition duration-300 ease-in-out file:-mx-3 file:-my-[0.32rem] file:me-3 file:cursor-pointer file:overflow-hidden file:rounded-none file:border-0 file:border-e file:border-solid file:border-inherit file:bg-transparent file:px-3  file:py-[0.32rem] file:text-surface focus:border-primary focus:text-gray-700 focus:shadow-inset focus:outline-none dark:border-white/70 dark:text-white  file:dark:text-white",

            }),
            'datetime': DateTimeInput(attrs={
                'class':'m-2 p-2 border-2 block',
            })
        }