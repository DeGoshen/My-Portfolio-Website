# Create your models here.
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, EmailValidator


class Contact(models.Model):
    """Model to store contact form submissions."""
    
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    email = models.EmailField(validators=[EmailValidator()])
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'

    def __str__(self):
        return f"{self.name} - {self.subject}"


class Blog(models.Model):
    """Model to store blog posts."""
    
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, blank=True)
    description = models.CharField(max_length=500, blank=True)
    image = models.ImageField(upload_to='blog_images/%Y/%m/%d/', blank=True, null=True)
    content = models.TextField()
    is_published = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-date_created']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'

    def __str__(self):
        return self.title


class Skill(models.Model):
    """Model to store skills with proficiency levels."""
    
    CATEGORY_CHOICES = [
        ('FRONTEND', 'Frontend'),
        ('BACKEND', 'Backend'),
        ('TOOLS', 'Tools & DevOps'),
        ('DESIGN', 'UI/UX Design'),
    ]
    
    name = models.CharField(max_length=100)
    level = models.IntegerField(
        default=100,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(100)
        ]
    )
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='FRONTEND')
    icon_class = models.CharField(max_length=50, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-level', 'name']
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'

    def __str__(self):
        return f"{self.name} ({self.level}%)"