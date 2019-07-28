from django import forms
from .models import Board, Comment

class BoardForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(BoardForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'class': 'uk-input'}
        self.fields['content'].widget.attrs = {'class': 'uk-textarea'}
    class Meta:
        model = Board
        fields = ['title', 'content']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']