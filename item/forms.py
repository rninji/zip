from django import forms
from .models import Item, ItemComment

class ItemForm(forms.ModelForm):
    class Meta:
        model=Item
        fields=['name','image','price','shop','type']

class ItemCommentForm(forms.ModelForm):
    class Meta:
        model=ItemComment
        fields=["text"]