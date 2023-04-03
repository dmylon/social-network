from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

class User(AbstractUser):
    id = models.BigAutoField(primary_key=True)
    def __str__(self):
        return "id: " + str(self.id)


class Profile(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    following = models.ManyToManyField(User, related_name="followers", blank=True)

    def __str__(self):
        return "User ID(" + str(self.user.id) + ")"

class Post(models.Model):
    id = models.AutoField(primary_key=True)
    owner = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name="posts")
    content = models.CharField(max_length=200)
    date = models.DateTimeField(default=timezone.now)
    liked_by = models.ManyToManyField(Profile, related_name="liked_posts", blank=True)

    def __str__(self):
        return "Post ID(" + str(self.id) + ")"