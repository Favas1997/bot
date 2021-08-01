

from django.db import models


class chats(models.Model):
    Username = models.CharField(max_length=200, default=None, blank=True, null=True)
    button_stupid = models.BigIntegerField(default=0, blank=True, null=True)
    button_fat = models.BigIntegerField(default=0, blank=True, null=True)
    button_dumb = models.BigIntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return self.Username
