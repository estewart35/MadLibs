from django.db import models

# Create your models here.
class MadLibTemplate(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(help_text='Use placeholders like {verb_1}, {adjective}, {verb_2}, {famous_person}')
    fields = models.JSONField(help_text='List of required fields like ["verb_1", "adjective", "verb_2", "famous_person"].')

    def __str__(self) -> str:
        return self.title