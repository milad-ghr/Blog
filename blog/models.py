from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(User , on_delete=models.CASCADE)
    content = models.TextField()
    post_dated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return  'id: ' + str(self.id) + 'title' + str(self.title)

    def get_absolute_url(self):
        return reverse('post-detail' , kwargs={'pk' : self.pk})