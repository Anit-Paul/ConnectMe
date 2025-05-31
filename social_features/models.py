from django.db import models
from django.conf import settings
# Create your models here.
class Follow(models.Model):
    following=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="following",on_delete=models.CASCADE)
    follower=models.ForeignKey(settings.AUTH_USER_MODEL,related_name="follower",on_delete=models.CASCADE)
    followed_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('follower', 'following')  # Prevent duplicates

    def __str__(self):
        return f"{self.follower.username} follows {self.following.username}"

class Post(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        related_name="posts",  # use 'posts' not 'following'
        on_delete=models.CASCADE
    )
    caption = models.TextField(blank=True)
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)  # set this automatically
    likes = models.ManyToManyField(
        settings.AUTH_USER_MODEL, 
        related_name='liked_posts', 
        blank=True
    )

# Create your models here.
