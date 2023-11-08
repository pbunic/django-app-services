from django import forms

from .models import Newsletter


class NewsletterForm(forms.Form):
    """Sign-in to newsletter."""
    class Meta:
        model = Newsletter
        fields = ['email']

    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': ''}))


class EmailPostForm(forms.Form):
    """Share post by email."""
    name = forms.CharField(
        max_length=40, label='name:',
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'Maximum number of allowed characters is 40.'
        }
    )
    email = forms.EmailField(label='your email:')
    to_mail = forms.EmailField(
        label='receiver email:',
        error_messages={'required': 'Please enter receiver email address.'}
    )
    comment = forms.CharField(
        required=False, label='optional comment:',
        widget=forms.Textarea
    )


class SearchForm(forms.Form):
    """Search form."""
    query = forms.CharField(label='')
