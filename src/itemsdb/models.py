from django.db import models


class Category(models.Model):
    # Created
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Fields
    name = models.CharField(max_length=20)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Item(models.Model):
    # Created
    created = models.DateTimeField(auto_now_add=True, editable=False)

    # Fields
    code = models.CharField(max_length=3)
    name = models.CharField(max_length=20)
    active = models.BooleanField(default=False)

    # Relational Fields
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['code', 'name']

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
