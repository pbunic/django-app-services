from django.core.exceptions import ValidationError


def validate_no_space(value):
    if value.isspace():
        raise ValidationError("Field can't contain only spaces.")
