from django.db import models


class DefaultNumber(models.Model):
    name = models.CharField(unique=True, max_length=50)
    value = models.IntegerField()

    def __str__(self):
        return f"Default {self.name}: {self.value}"


class DefaultChecked(models.Model):
    title_input = models.CharField(unique=True, max_length=50)
    radio_value = models.CharField(max_length=50)

    def __str__(self):
        return f"Default {self.title_input}: {self.radio_value}"