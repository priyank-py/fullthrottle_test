from django.db import models

# Create your models here.
class Country(models.Model):

    

    class Meta:
        verbose_name = _("Country")
        verbose_name_plural = _("Countrys")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("Country_detail", kwargs={"pk": self.pk})

