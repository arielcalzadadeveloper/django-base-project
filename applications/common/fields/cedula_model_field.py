from django.db import models
from django.core.validators import RegexValidator


class CedulaModelField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 20
        super().__init__(*args, **kwargs)

        regex = r"^[1-9]\d*$"
        message = "Número inválido"
        validator = RegexValidator(regex=regex, message=message)

        self.validators.append(validator)
