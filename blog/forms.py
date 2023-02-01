from django import forms
from django.forms import TextInput, EmailInput


class EmailPostForm(forms.Form):
    '''
    Email post form for sharing blogs
    '''
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        ),
    )   
    email = forms.EmailField(
        widget=forms.EmailInput(
            
            attrs={
               
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        )
    )
    recipient_email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        )
    )
    comments = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        ),
    )


class ContactForm(forms.Form):
    '''
    Contact form for contact page
    '''
    name = forms.CharField(
        max_length=25,
        widget=forms.TextInput(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        ),
    )
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        )
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "w-full bg-gray-100 bg-opacity-50 rounded border border-gray-300 focus:border-indigo-500 focus:bg-white focus:ring-2 focus:ring-indigo-200 text-base outline-none text-gray-700 py-1 px-3 leading-8 transition-colors duration-200 ease-in-out"
            }
        ),
    )
