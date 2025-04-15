from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile, Team, Sponsorship, Event

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'placeholder': 'Enter your email',
            'autocomplete': 'email'
        })
    )
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'placeholder': 'Choose a username',
            'autocomplete': 'username'
        })
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'placeholder': 'Enter password',
            'autocomplete': 'new-password'
        })
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
            'placeholder': 'Confirm password',
            'autocomplete': 'new-password'
        })
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['role']
        widgets = {
            'role': forms.HiddenInput(attrs={'class': 'hidden'})
        }

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = ['name', 'members']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500',
                'placeholder': 'Enter team name'
            }),
            'members': forms.SelectMultiple(attrs={
                'class': 'mt-1 block w-full rounded-md border-gray-300 shadow-sm focus:border-blue-500 focus:ring-blue-500'
            })
        }

class SponsorshipForm(forms.ModelForm):
    class Meta:
        model = Sponsorship
        fields = ['event', 'amount', 'tier']
        widgets = {
            'event': forms.Select(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Select an event'
            }),
            'amount': forms.NumberInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter sponsorship amount'
            }),
            'tier': forms.Select(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Select sponsorship tier'
            })
        }

class SponsorProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['company_name', 'contact_info', 'logo']
        widgets = {
            'company_name': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter company name'
            }),
            'contact_info': forms.TextInput(attrs={
                'class': 'w-full p-2 border rounded',
                'placeholder': 'Enter contact information'
            }),
            'logo': forms.FileInput(attrs={
                'class': 'w-full p-2',
                'placeholder': 'Upload company logo'
            })
        }
