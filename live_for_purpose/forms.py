
from django import forms
from .models import Comments
class CommentModelForm(forms.ModelForm):

    class Meta:
        model = Comments
        fields = ['Name','Mail_id','Message']
            