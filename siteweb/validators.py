from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
#from django.utils.translation import gettext_lazy as _

RIB_REGEX = RegexValidator(r'\d{24}', 'le RIB se constitue de 24 chiffres')

def validate_file_extension(value):
    import os
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')