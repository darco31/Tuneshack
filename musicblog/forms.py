from django import forms
from .models import Post


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = (
            'title',
            'author',
            'body',
        )

        """
        Add form control and placeholder text below from bootstrap
        """

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your title here!!'}),
            'author': forms.Select(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Express yourself'}),
        }


class EditForm(forms.ModelForm):
    """
    Add form to Dit the posts and apply styling with
    Bootstrap
    """
    class Meta:
        model = Post
        fields = (
            'title',
            'body',
        )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Put your title here!!'}),
            # 'author': forms.Select(attrs={'class': 'form-control'}),
             'body': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Express yourself'}),
        }
