from django import forms
from .models import Question, User_bids

class AskQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['text']

        widgets = {
            'text': forms.TextInput(attrs={'id': 'question', 'placeholder': 'Ask a question...', 'class': 'help-search-input'}),
        }

class ProductTransactionForm(forms.ModelForm):
    class Meta:
        model = User_bids
        fields = ['price']

        widgets = {
            'price': forms.NumberInput(attrs={'id': 'question', 'class': 'form-control changable p-4'}),
        }