from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


class Post(models.Model):
    content = models.CharField(max_length=500, null=False)
    writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name="post_writer")
    timestamp = models.DateTimeField(auto_now_add=True)
    likes = models.IntegerField(default=0)

    def serialize(self):
        return {
            "content": self.content,
            "timestamp": self.timestamp.strftime("%b %d %Y, %I:%M %p"),
            "writer": self.writer
        }
    
    def __str__(self) -> str:
        return f"{self.writer}-{self.content}"