from django.forms import models
from .models import BlogPost

class BlogForm(models.ModelForm):
    """Create a model for a blog form."""
    class Meta:
        model = BlogPost
        fields = ['title', 'text']