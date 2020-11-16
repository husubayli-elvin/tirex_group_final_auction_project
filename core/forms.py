from django import forms
from .models import Question

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ask a question...', 'class': 'help-search-input'}),
        }