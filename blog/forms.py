from django import forms
from .models import Post, Comment


def min_length_5_validator(value):
    if len(value) < 5:
        raise forms.ValidationError('title은 5글자 이상 입력해주세요')


class PostForm(forms.ModelForm):
    title = forms.CharField(validators=[min_length_5_validator])
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = Post
        fields = ('title', 'text')


class PostModelForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('author', 'text')
