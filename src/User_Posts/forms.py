from django import forms
from .models import UserPost, Comment

class UserPostForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'rows':2, 'placeholder': 'What are you thinking?',}), label=False)

    
    class Meta:
        model = UserPost
        fields = ('content',)
       

class CommentForm(forms.ModelForm):
    body = forms.CharField(label='Add a comment',)
    class Meta:
        model = Comment
        fields = ('body',)
        