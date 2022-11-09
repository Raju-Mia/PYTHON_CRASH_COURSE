from django import forms
from .models import BlogPost

class EditBlogform(forms.ModelForm):
    class Meta:
        model = BlogPost
        fields = "__all__"
        # fields= ['title', 'text']

        

