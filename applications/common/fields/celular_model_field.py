from django.db import models
from django.core.validators import RegexValidator


class CelularModelField(models.CharField):
    def __init__(self, *args, **kwargs):
        kwargs["max_length"] = 10
        super().__init__(*args, **kwargs)

        regex = r"^3\d{9}$"
        message = "Número inválido"
        validator = RegexValidator(regex=regex, message=message)

        self.validators.append(validator)
