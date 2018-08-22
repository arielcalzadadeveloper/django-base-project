from django.db import models


class BaseModelQuerySet(models.QuerySet):
    pass


class BaseModelManager(models.Manager):
    def get_queryset(self):
        return BaseModelQuerySet(self.model, using=self._db)


class BaseModel(models.Model):
    creation_date = models.DateTimeField(
        verbose_name="Fecha de creación",
        auto_now_add=True,
        editable=False,
        db_index=True
    )

    modification_date = models.DateTimeField(
        verbose_name="Fecha última modificación",
        auto_now=True,
        editable=False,
        db_index=True
    )

    objects = BaseModelManager()

    def __str__(self):
        return "{pk}".format(pk=self.pk)

    class Meta:
        abstract = True
