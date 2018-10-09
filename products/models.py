from django.db import models
from products import abstract_models as pam


class Category(pam.AbstractCategory):

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Category({self.title})'


class SubCategory(pam.AbstractCategory):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'SubCategory'
        verbose_name_plural = 'SubCategories'
        ordering = ('created', )

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'SubCategory({self.title})'


class Product(pam.AbstractProduct):
    sub_category = models.ForeignKey(SubCategory, on_delete=models.PROTECT)

    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    def __str__(self):
        return f'{self.title}'

    def __repr__(self):
        return f'Product{self.title}'
