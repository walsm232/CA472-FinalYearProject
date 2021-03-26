from django import forms
from .models import UserProfile

# Selection of Year choices for User Profile 'year' variable
YEAR_CHOICES = (
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
)
# Update User Profile Form
class UserProfileForm(forms.ModelForm): 
    
    first_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'First Name',}))
    last_name = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Last Name',}))
    profile_picture = forms.ImageField()
    bio = forms.CharField(widget=forms.Textarea(attrs={'rows':4,'placeholder': 'Bio',}))
    course = forms.CharField(widget=forms.Textarea(attrs={'rows':1, 'placeholder': 'Course'}))
    
    class Meta:
        model = UserProfile
        fields = ('first_name', 'last_name', 'bio', 'university', 'course', 'year', 'profile_picture')