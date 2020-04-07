from django import forms
from blog.models import BlogModel

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = BlogModel
        fields = '__all__'
