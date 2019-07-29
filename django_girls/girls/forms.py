from django import forms

from .models import Cat

class PostForm(forms.ModelForm):

    class Meta:
        model = Cat
        fields = ('title', 'text',)