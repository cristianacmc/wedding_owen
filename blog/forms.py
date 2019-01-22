
from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('contact-name', 'contact-email', 'contact-Subject',
        	'contact-Subject', 'contact-message', )
