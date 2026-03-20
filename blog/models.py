from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(mas_length=255)

    class meta:
        ordering = ('title')
        verbose_name_prural = 'categories'
    
    def __str__(self):
        return self.title
    
class Post(models.model):

    ACTIVATE = 'activate'
    DRAFT = 'draft'