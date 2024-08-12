from .models import History
from django.forms import ModelForm, TextInput, Textarea, ImageField, DateField

class HistoryForm(ModelForm):
    class Meta():
        model = History
        
        fields = ['title', 'anons', 'full_story', 'datetime']
        
        widgets = {
            'title':TextInput(attrs={
                'class':'w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none',
                'placeholder':'Название'
            }),
            'anons':TextInput(attrs={
                'class':'w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none',
                'placeholder':'Анонс'
            }),
            'full_story':Textarea(attrs={
                'class':'w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none',
                'placeholder':'Полный текст',
                'rows': 4,
            }),
            'datetime':TextInput(attrs={
                'class':'w-full block rounded-lg border dark:border-none dark:bg-neutral-600 py-[9px] px-3 pr-4 text-sm focus:border-blue-400 focus:ring-1 focus:ring-blue-400 focus:outline-none',
                'placeholder':'Дата и время',
                'type':'date'
            }),
            
        }