from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Comment


class EmailPostForm(forms.Form):
    """Share post by email."""

    name = forms.CharField(
        max_length=40, label='Your name:',
        error_messages={
            'required': 'Please enter your name.',
            'max_length': 'Maximum number of allowed characters is 40.'
        }
    )
    email = forms.EmailField(label='Your email:')
    to_mail = forms.EmailField(
        label='Receiver email:',
        error_messages={'required': 'Please enter receiver email address.'}
    )
    comment = forms.CharField(
        required=False, label='Optionally include comment:',
        widget=forms.Textarea
    )


class CommentForm(forms.ModelForm):
    """Add a comment."""

    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']
        labels = {
            'body': _('Comment:'),
        }
