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
        return f"{self.follower} follows {self.following}"