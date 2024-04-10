from django.db import models
from django.urls import reverse
import datetime

# Create your models here.
class Category(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    # parent = TreeForeignKey('self',blank=True, null=True ,related_name='children', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    status=models.CharField(max_length=10, choices=STATUS)
    keywords = models.CharField(max_length=255)
    image = models.ImageField(upload_to='uploads')
    description = models.TextField(max_length=255)
    slug = models.SlugField(null=False, unique=True)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})
    

class Products(models.Model):
    STATUS = (
        ('True', 'True'),
        ('False', 'False'),
    )
    VARIANTS = (
        ('None', 'None'),
        ('Size', 'Size'),
        ('Color', 'Color'),
        ('Size-Color', 'Size-Color'),

    )
    name = models.CharField(max_length=60)
    keywords = models.CharField(max_length=255)
    variant=models.CharField(max_length=10,choices=VARIANTS, default='None')
    price = models.IntegerField(default=0)
    discount=models.IntegerField(default=0)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.CharField(
        max_length=250, default='', blank=True, null=True)
    image = models.ImageField(upload_to='uploads')
    # detail=RichTextUploadingField()
    slug = models.SlugField(null=False, unique=True)
    status=models.CharField(max_length=10,choices=STATUS)
    featured=models.CharField(max_length=10,choices=STATUS)
    create_at=models.DateTimeField(auto_now_add=True)
    update_at=models.DateTimeField(auto_now=True)
 
    def __str__(self):
        return self.name


    ## method to create a fake table field in read only mode
    def image_tag(self):
        if self.image.url is not None:
            return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
        else:
            return ""

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})  