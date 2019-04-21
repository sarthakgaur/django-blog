from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    """Create a blog model."""
    title = models.CharField(max_length=50)
    date = models.DateTimeField(auto_now=True)
    text = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        """Return the string when the object is called."""
        return self.title