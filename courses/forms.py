from django import forms
from .models import Retings, Comment

class RetingsForm(forms.ModelForm):
    # score = forms.IntegerField(
    #     widget=forms.RadioSelect(choices=[(i, str(i)) for i in range(1, 6)], attrs={'class': 'stars'}),
    #     label=None  
    # )

    class Meta:
        model = Retings
        fields = ('score', )

        widgets = {
            'score': forms.RadioSelect(choices=[(i, f"{i} звёзд") for i in range(1, 6)], attrs={'class': 'flex'}),
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text', ) 

