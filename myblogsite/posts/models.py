from django.db import models

class Post(models.Model):

    post_author = models.CharField(max_length=100, default="Anonymous")



    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
