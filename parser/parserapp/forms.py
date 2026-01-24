from django import forms
class CommentForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    comment = forms.CharField(label='Коментарий')
