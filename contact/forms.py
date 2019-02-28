from django import forms


class ContactForm(forms.Form):

    name = forms.CharField(
        label='name',
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'wp-form-control wpcf7-text',
                'placeholder': 'Your Name'
            }
        )

    )

    email = forms.EmailField(
        label='Email',
        max_length=100,
        min_length=10,
        required=True,
        widget=forms.EmailInput(
            attrs={
                'class': 'wp-form-control wpcf7-email',
                'placeholder': 'Email adresses'
            }
        )
    )

    subject = forms.CharField(
        label='Subject',
        max_length=100,
        min_length=3,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'wp-form-control wpcf7-text',
                'placeholder': 'Subject'
            }
        )

    )

    content = forms.CharField(
        label='Content',
        max_length=1000,
        min_length=3,
        required=True,
        widget=forms.Textarea(
            attrs={
                'class': 'wp-form-control wpcf7-textarea',
                'placeholder': 'What would you like to tell us'
            }
        )

    
    )