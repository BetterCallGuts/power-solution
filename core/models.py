from django.db import models
from django.utils.html import mark_safe
from django.utils.text import slugify

class Brand(models.Model):
    img         = models.ImageField(upload_to='media/brands/', blank=True)
    name        = models.CharField(max_length=100)
    deactivated = models.BooleanField(default=False)
    def thumb_nail(self):
        return mark_safe(f'<img src="{self.img.url}" alt="{self.name}" width="300px" height="300px">')
    thumb_nail.allow_tags = True
    def __str__(self):
        return self.name
    

# ---------
# ---------
# ---------

# 
# 
# 



class Product(models.Model):
    name        = models.CharField(max_length=100)
    description = models.TextField()

    thumbnail   = models.ImageField(upload_to='products', blank=True, null=True)
    category    = models.ForeignKey("Category", null=True,blank=True, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True, blank=True)

    def thumb_nail(self):
            return mark_safe(f'<img src="{self.thumbnail.url}" alt="{self.name}" width="300px" height="300px">')
    thumb_nail.allow_tags = True
    def __str__(self):
        return self.name 
    def save(self, *args, **kwargs):
        
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image   = models.ImageField(upload_to='products_more', blank=True, null=True)
    def __str__(self):

        return f"{self.image}"

class Category(models.Model):
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name