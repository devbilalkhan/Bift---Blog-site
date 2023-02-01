from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    """
    
    """
    def get_queryset(self):
        return super().get_queryset().filter(status=Post.Status.PUBLISHED)


# Create your models here 
class Post(models.Model):
    """
    Post model
    """
    class Status(models.TextChoices):
        DRAFT = "DF", "Draft"
        PUBLISHED = "PB", "Published"

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique_for_date='publish')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    

    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.DRAFT
    
    )
    author = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name='blog_posts')
    """default object manager"""
    manager = models.Manager()

    """custom object manager"""
    published = PublishedManager()
    
    class Meta:
        ordering = ['-publish']
        indexes = [
            models.Index(fields=['-publish'])
        ]

    def __str__(self) -> str:
        return self.title

    '''Handle canonical urls for post objects dynamically
       /blog/posts/1 cano
    '''
    def get_absolute_url(self):
       
        return reverse('blog:post_detail', args=[self.publish.year, 
                                                self.publish.month, 
                                                self.publish.day,
                                                self.slug])
    

