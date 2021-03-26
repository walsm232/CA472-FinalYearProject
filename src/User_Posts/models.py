from django.db import models
from django.core.validators import FileExtensionValidator
from User_Profiles.models import UserProfile

class UserPost(models.Model):
    content = models.TextField()
    image = models.ImageField(upload_to='posts', validators=[FileExtensionValidator(['jpg', 'jpeg', 'png'])], blank=True)
    liked = models.ManyToManyField(UserProfile, blank=True, related_name='likes')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='posts')
    

    def __str__(self):
        return str(self.content[:20])

    def NumberOfLikes(self):
        return self.liked.all().count()

    def NumberOfComments(self):
        return self.comment_set.all().count()

    class Meta:
        ordering = ('-created',)



LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)

## Likes Model
class Like(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES, max_length=8)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"

## Comments Model 
class Comment(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    body = models.TextField(max_length=300)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    
    def __str__(self):
        return str(self.pk)


