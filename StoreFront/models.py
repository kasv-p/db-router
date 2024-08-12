from django.db import models


class Item(models.Model):
    id = models.AutoField(primary_key=True)
    description = models.TextField()

    def __str__(self):
        return f'id = {self.id}, description = {self.description}'
