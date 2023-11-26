from django import forms

from .models import Post,Comments

class PostForm(forms.ModelForm):
    class Meta:
        model=Post
        fields='__all__'
        exclude=('author',)
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comments
        fields='__all__'
        exclude=('post','publish_date','author')