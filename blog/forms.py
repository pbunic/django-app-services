from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment
from .validators import validate_no_space


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


class CommentForm(forms.ModelForm):
    """Add a comment."""

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'name': _('name:'),
            'email': _('email:'),
            'body': _('comment:'),
        }


class SearchForm(forms.Form):
    """Search form."""
    query = forms.CharField(label='', validators=[validate_no_space])
