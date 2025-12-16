# blog/models.py
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
    ]

    title = models.CharField(max_length=100)
    content = models.TextField()
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='draft',
    )
    # A Post can have only one Category
    category = models.ForeignKey( 
        Category, 
        on_delete=models.CASCADE, 
        related_name='posts',
        null=True,
        blank=True
    )
    # A Post can have multiple Tags
    tags = models.ManyToManyField( 
        Tag, 
        related_name='posts',
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True, blank=True )

# Modal Method (parantehesis needed when calling the method)
    def summary(self): 
        return self.content[:50] + "..."   #This is a method to return the first 50 characters of the content

    @property #This is a property to return the word count of the content
    def word_count(self): # Usage: post.word_count (no parentheses needed)
        return len(self.content.split())    

    def __str__(self):
        return self.title
