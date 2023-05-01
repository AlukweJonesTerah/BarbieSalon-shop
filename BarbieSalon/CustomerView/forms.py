from django import forms
from .models import Subscribe


class SubscribeForm(forms.ModelForm):
    email = forms.EmailField(max_length=50, min_length=10, widget=forms.EmailInput(
        attrs={'class': 'newletter-input', 'placeholder': 'example@gmail.com', 'style': 'height:50px'}))

    class Meta:
        model = Subscribe
        fields = ['email', ]
