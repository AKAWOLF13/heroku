from django.db import models
from django import forms
from django.utils import timezone

class Blog(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateField('date published')
    body = models.TextField()

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]
    
class Comment(models.Model):
    post = models.ForeignKey('blogapp.Blog', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
# Create your models here.
