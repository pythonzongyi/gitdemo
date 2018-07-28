from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32,default='Title')
    content = models.TextField(null=True)

    class Meta:
        db_table = 'Article'

    def __str__(self):
        return self.title