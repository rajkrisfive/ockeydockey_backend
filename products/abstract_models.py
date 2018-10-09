from django.db import models


class AbstractCategory(models.Model):
    title = models.CharField('Title', max_length=100)
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        abstract = True


class AbstractProduct(models.Model):
    title = models.CharField('Title', max_length=250)
    description = models.TextField('Description', blank=True, default='')
    created = models.DateTimeField('Created', auto_now_add=True)

    class Meta:
        abstract = True