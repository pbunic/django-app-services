from django import forms

from .models import Newsletter


class NewsletterForm(forms.Form):
    """Sign-in to newsletter."""
    class Meta:
        model = Newsletter
        fields = ['email']

    email = forms.EmailField(label='', widget=forms.EmailInput(attrs={'placeholder': 'email'}))


class EmailPostForm(forms.Form):
    """Share post by email."""
    name = forms.CharField(
        max_length=40,
        label='',
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'Maximum number of allowed characters is 40.'
        },
        widget=forms.TextInput(attrs={'placeholder': 'your name'}),
    )
    email = forms.EmailField(
        label='',
        error_messages={'required': 'Please enter valid email address.'},
        widget=forms.EmailInput(attrs={'placeholder': 'your email'}),
    )
    to_mail = forms.EmailField(
        label='',
        error_messages={'required': 'Please enter valid email address.'},
        widget=forms.EmailInput(attrs={'placeholder': 'receiver email'}),
    )
    comment = forms.CharField(
        required=False,
        label='',
        widget=forms.Textarea(attrs={'placeholder': 'optional comment'}),
    )


class SearchForm(forms.Form):
    """Search form."""
    query = forms.CharField(label='')
