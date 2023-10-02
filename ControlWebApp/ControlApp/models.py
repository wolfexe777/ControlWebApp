from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

class Comment(models.Model):
    author = models.CharField(max_length=50, verbose_name='Автор')
    content = models.TextField(verbose_name='Текст')
    post = models.ForeignKey('Post', on_delete=models.CASCADE)

    def __str__(self):
        return f'Comment by {self.author} on {self.post.title}'
