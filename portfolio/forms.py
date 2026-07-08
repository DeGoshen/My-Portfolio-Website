from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    Form for the contact page.
    Uses ModelForm to automatically validate data against the Contact model.
    """
    
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        
        # Add Bootstrap classes and placeholders for better styling
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
                'id': 'id_name'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
                'id': 'id_email'
            }),
            'subject': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'What is this about?',
                'id': 'id_subject'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Write your message here...',
                'rows': 5,
                'id': 'id_message'
            }),
        }
    
    def clean_email(self):
        """Additional validation for email field."""
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError("Email is required.")
        return email