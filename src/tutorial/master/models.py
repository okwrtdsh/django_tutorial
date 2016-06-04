from django.db import models
from tutorial.models import ModelBase


class Category(ModelBase):
    """カテゴリー"""

    class Meta:
        verbose_name = verbose_name_plural = "カテゴリー"
        ordering = ["order"]

    name = models.CharField("名称", max_length=255)
    order = models.PositiveIntegerField("表示順")

    def __str__(self):
        return self.name

