from django import forms

from .models import Comment


# class CommentForm(forms.Form):
#     name = forms.CharField(label='Ваше имя')
#     comment = forms.CharField(label='Коментарий')
class CommentForm(forms.ModelForm):
    name = forms.CharField(label='',
                           widget=forms.TextInput(attrs={'class': 'form-control',
                                                         'placeholder': 'Имя'}))
    comment = forms.CharField(label='',
                              widget=forms.Textarea(attrs={'class': 'form-control',
                                                           'placeholder': 'Ваш комментарий'}))
    class Meta:
        model = Comment
        fields = '__all__'
