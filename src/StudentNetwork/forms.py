from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.core.validators import EmailValidator
from django.utils.deconstruct import deconstructible

## College and University Emails for Email Validation
EMAIL_CHOICES = [
    'mail.ahc.ie', ## All Hallows College
    'mail.ait.ie', ## Athlone Institute of Technology
    'mail.cc.ie', ## Carlow College
    'mail.cit.ie', ## Carlow Institute of Technology
    'mail.dcu.ie', ## Dublin City University
    'mail.dliadt.ie', ## Dun Laoghaire Institute of Art, Design and Technology
    'mail.dit.ie', ## Dublin Institute of Technology
    'mail.gmit.ie', ## Galway-Mayo Institute of Technology
    'mail.ipa.ie', ## Institute of Public Administration
    'mail.itc.ie', ## Insitute of Technology Carlow
    'mail.its.ie', ## Institute of Technology Sligo
    'mail.itt.ie', ## Institute of Technology Tralee
    'mail.lit.ie', ## Letterkenny Institute of Technology and Limerick Institute of Technology
    'mail.mie.ie', ## Marino Institute of Education
    'mail.nuim.ie', ## National University of Ireland Maynooth
    'mail.ncad.ie', ## National College of Art and Design
    'mail.nci.ie', ## National College of Ireland
    'mail.nuig.ie', ## National University of Ireland Galway
    'mail.rcsi.ie', ## Royal College of Surgeons Ireland
    'mail.riam.ie', ## Royal Irish Academy of Music
    'mail.spcm.ie', ## Saint Patricks College Maynooth
    'mail.tud.ie', ## Technological University Dublin
    'mail.tcd.ie', ## Trinity College Dublin
    'mail.ucc.ie', ## University College Cork
    'mail.ucd.ie', ## University College Dublin
    'mail.ul.ie', ## University Limerick
    'mail.wit.ie', ## Waterford Institute of Technology
]

## Whitelist for College Emails
@deconstructible
class WhitelistEmailValidator(EmailValidator):
    def validate_domain_part(self, domain_part):
        return False

    def __eq__(self, other):
        return isinstance(other, WhitelistEmailValidator) and super().__eq__(other)


## New class which inherits UserCreationForm
class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    email = forms.EmailField(max_length=60, validators=[WhitelistEmailValidator(whitelist=EMAIL_CHOICES)])
    password1 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)
    password2 = forms.CharField(max_length=30, required=True, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        username = forms.CharField()


## Application Form for Apply Page
class ApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    message_email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)
    CV = forms.FileField()