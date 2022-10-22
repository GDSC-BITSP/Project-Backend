from django import forms
from .models import Club
class ClubForm(forms.ModelForm):
    class Meta:
        model = ClubForm
        fields = {
            'author',
            'name',
            'logo',
            'skill',
            'description',
            'prev_work',
            'por_text',
            'por_img',
            'last_updated',
            'recruit_link',
            'event_details',
     }
