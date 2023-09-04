from django import forms
from django.core.exceptions import ValidationError

from .models import Post

class PostForm(forms.ModelForm):
    text = forms.CharField(min_length=20)

    class Meta:
        model = Post
        fields = [
            'author',
            'category',
            'head',
            'text',
        ]

    def clean(self):
        cleaned_data = super().clean()
        head = cleaned_data.get("head")
        text = cleaned_data.get("text")

        if head == text:
            raise ValidationError(
                "Текст не должен быть идентичным названию."
            )

        return cleaned_data




