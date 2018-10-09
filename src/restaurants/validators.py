from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _('%(value)s is not an even number'),
            params={'value': value},
        )

CATEGORIES = ('Mexican', 'Asian', 'American')

def validate_category(value):
    if not value in CATEGORIES:
        raise ValidationError(f"{value} is not a valid category")