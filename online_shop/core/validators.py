import re

from django.core.exceptions import ValidationError


def check_phone(value):
    patter = re.compile("^09\d{9}$")

    if bool(patter.match(value)):
        return value

    raise ValidationError(f'{value} is not a valid phone')
