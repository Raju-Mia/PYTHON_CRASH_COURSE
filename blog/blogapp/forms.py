from django import forms
from .models import BlogPost

class BlogPostform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"
        # fields= ['title', 'text']

        

