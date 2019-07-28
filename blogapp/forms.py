from django import forms
from .models import Blog, Comment

class BlogPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title','body']
        labels = {
            "title":"제목",
            "body":"내용"
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author','text',)