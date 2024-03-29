from django.core.urlresolvers import reverse
from django.db import models

# Create your models here.


class List(models.Model):
    def get_absolute_url(self):
        return reverse("view_list", args=[self.id])


class Item(models.Model):
    text = models.TextField(default="")
    list = models.ForeignKey(List, default=None)

    class Meta:
        unique_together = ("list", "text")
        ordering = ("id",)

    def __str__(self) -> str:
        return self.text

    def get_absolute_url(self):
        return reverse("view_list", args={self.list.id})
