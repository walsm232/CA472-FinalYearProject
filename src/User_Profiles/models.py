from django.db import models
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import reverse

# Needed in order to generate a slug with random ID
from .utils import Get_Random_Identifier
from django.template.defaultfilters import slugify

# Selection of College and University choices for User Profile 'university' variable ##
COLLEGE_CHOICES = (
    ('All Hallows College', 'All Hallows College'),
    ('Athlone Institute of Technology', 'Athlone Institute of Technology'),
    ('Carlow College', 'Carlow College'),
    ('Cork Institute of Technology', 'Cork Institute of Technology'),
    ('Dublin City University', 'Dublin City University'),
    ('Dun Laoghaire Institute of Art, Design and Technology', 'Dun Laoghaire Institute of Art, Design and Technology'),
    ('Dundalk Institute of Technology', 'Dundalk Institute of Technology'),
    ('Galway-Mayo Institute of Technology', 'Galway-Mayo Institute of Technology'),
    ('Institute of Public Administration', 'Institute of Public Administration'),
    ('Insitute of Technology Carlow', 'Insitute of Technology Carlow'),
    ('Institute of Technology Sligo', 'Insitute of Technology Sligo'),
    ('Institute of Technology Tralee', 'Institute of Technology Tralee'),
    ('Letterkenny Institute of Technology', 'Letterkenny Institute of Technology'),
    ('Limerick Institute of Technology', 'Limerick Institute of Technology'),
    ('Marino Institute of Education', 'Marino Institute of Education'),
    ('National University of Ireland Maynooth', 'National University of Ireland Maynooth'),
    ('National College of Art and Design', 'National College of Art and Design'),
    ('National College of Ireland', 'National College of Ireland'),
    ('National University of Ireland Galway', 'National University of Ireland Galway'),
    ('Royal College of Surgeons Ireland', 'Royal College of Surgeons Ireland'),
    ('Royal Irish Academy of Music', 'Royal Irish Academy of Music'),
    ('Saint Patricks College Maynooth', 'Saint Patricks College Maynooth'),
    ('Technological University Dublin', 'Technological University Dublin'),
    ('Trinity College Dublin', 'Trinity College Dublin'),
    ('University College Cork', 'University College Cork'),
    ('University College Dublin', 'University College Dublin'),
    ('University of Limerick', 'University of Limerick'),
    ('Waterford Institute of Technology', 'Waterford Institute of Technology')
)

# Selection of Topic Areas for Tutors to mark on Profile
TOPIC_AREAS = (
    ('Accountancy & Taxation', 'Accountancy & Taxation'),
    ('Advertising, Marketing & Public Relations', 'Advertising, Marketing & Public Relations'),
    ('Animals & Veterinary Science', 'Animals & Veterinary Science'),
    ('Art, Craft & Design', 'Art, Craft & Design'),
    ('Biological, Chemical & Pharmaceutical Science', 'Biological, Chemical & Pharmaceutical Science'),
    ('Biomedical Technologies & Medtech', 'Biomedical Technologies & Medtech'),
    ('Business Management & Human Resources', 'Business Management & Human Resources'),
    ('Clerical & Administration', 'Clerical & Administration'),
    ('Community & Voluntary', 'Community & Voluntary'),
    ('Computers & ICT', 'Computers & ICT'),
    ('Construction, Architecture & Property', 'Construction, Architecture & Property'),
    ('Earth & Environment', 'Earth & Environment'),
    ('Education & Teaching', 'Education & Teaching'),
    ('Engineering, Manufacturing & Energy', 'Engineering, Manufacturing & Energy'),
    ('Farming, Horticulture & Forestry', 'Farming, Horticulture & Forestry'),
    ('Fashion & Beauty', 'Fashion & Beauty'),
    ('Food & Beverages', 'Food & Beverages'),
    ('Government, Politics & EU', 'Government, Politics & EU'),
    ('Healthcare', 'Healthcare'),
    ('History, Culture & Languages', 'History, Culture & Languages'),
    ('Insurance', 'Insurance'),
    ('Law & Legal', 'Law & Legal'),
    ('Leisure, Sport & Fitness', 'Leisure, Sport & Fitness'),
    ('Maritime, Fishing & Aquaculture', 'Maritime, Fishing & Aquaculture'),
    ('Media, Film & Publishing', 'Media, Film & Publishing'),
    ('Music & Performing Arts', 'Music & Performing Arts'),
    ('Physics, Mathematics & Space Science', 'Physics, Mathematics & Space Science'),
    ('Psychology & Social Care', 'Psychology & Social Care'),
    ('Sales, Retail & Purchasing', 'Sales, Retail & Purchasing'),
    ('Security, Defence & Law Enforcement', 'Security, Defence & Law Enforcement'),
    ('Tourism & Hospitality', 'Tourism & Hospitality'),
    ('Transport & Logistics', 'Transport & Logistics'),
)

# Selection of Year choices for User Profile 'year' variable
YEAR_CHOICES = (
    ('1st Year', '1st Year'),
    ('2nd Year', '2nd Year'),
    ('3rd Year', '3rd Year'),
    ('4th Year', '4th Year'),
)

# Account Types for UserProfile Model
ACCOUNT_TYPES = (
    ('Student', 'Student'),
    ('Tutor', 'Tutor'),
)

# Tutoring Rate per Hour Choices
RATE_CHOICES = (
    ('€5', '€5'),
    ('€10', '€10'),
    ('€15', '€15'),
    ('€20', '€20'),
    ('€25', '€25'),
    ('€30', '€30'),
    ('€35', '€35'),
    ('€40', '€40'),
)

class UserProfileManager(models.Manager):
    def All_Profiles(self, me):
        profiles = UserProfile.objects.all().exclude(user=me)
        return profiles

    def All_Profiles_Not_Friends_With(self, sender):
        profiles = UserProfile.objects.all().exclude(user=sender)
        profile = UserProfile.objects.get(user=sender)
        qs = Friendship.objects.filter(Q(sender=profile) | Q(receiver=profile))

        accepted = set([])
        for friendship in qs:
            if friendship.status == 'Request Accepted':
                accepted.add(friendship.receiver)
                accepted.add(friendship.sender)

        available = [profile for profile in profiles if profile not in accepted]
        return available

# User Profile Model
class UserProfile(models.Model):
    # Student and Tutor Variables
    account_type = models.CharField(max_length=20, blank=False, choices=ACCOUNT_TYPES, default="Student")
    user = models.OneToOneField(User, on_delete=models.CASCADE)  ## OneToOne is used as users will only have one profile
    first_name = models.CharField(max_length=255, blank=False)
    last_name = models.CharField(max_length=255, blank=False)
    profile_picture = models.ImageField(default='defaultprofilepicture.png', upload_to='profilepictures/')

    # Student Variables
    bio = models.TextField(default="Add a bio to tell others about yourself", max_length=500)
    email = models.EmailField(max_length=255, blank=True)
    university = models.CharField(max_length=60, blank=True, choices=COLLEGE_CHOICES)
    course = models.CharField(max_length=255, blank=True)
    year = models.CharField(max_length=10, blank=True, choices=YEAR_CHOICES)
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    # Tutor Variables
    qualifications = models.TextField(max_length=500, blank=True)
    experience = models.TextField(max_length=500, blank=True)
    topics = models.CharField(max_length=500, blank=True, choices=TOPIC_AREAS)
    availability = models.TextField(max_length=500, blank=True)
    hourly_rate = models.CharField(max_length=20, blank=True, choices=RATE_CHOICES)

    # Student and Tutor Variables
    slug = models.SlugField(unique=False, blank=True)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    __initial_first_name = None
    __initial_last_name = None

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.__initial_first_name = self.first_name
        self.__initial_last_name = self.last_name

    # Generates a slug with the First_Name and Last_Name fields. If a user with the same First and Last name exists then a random identifier will also be assigned
    def save(self, *args, **kwargs):
        ex = False
        set_slug = self.slug
        if self.first_name != self.__initial_first_name or self.last_name != self.__initial_last_name or self.slug=="":
            if self.first_name and self.last_name:
                set_slug = slugify(str(self.first_name) + " " + str(self.last_name))
                ex = UserProfile.objects.filter(slug=set_slug).exists()
                while ex:
                    set_slug = slugify(set_slug + " " + str(Get_Random_Identifier()))
                    ex = UserProfile.objects.filter(slug=set_slug).exists()
            else:
                set_slug = str(self.user)
        self.slug = set_slug
        super().save(*args, **kwargs)

    def FriendsList(self):
        return self.friends.all()

    def FriendsListCount(self):
        return self.friends.all().count()
    
    def PostsList(self):
        return self.posts.all()

    def PostsListCount(self):
        return self.posts.all().count()

    def __str__(self):
        return f"{self.user.username}-{self.created}"

    def URL(self):
        return reverse("ProfileDetail", kwargs={"slug": self.slug})

    objects = UserProfileManager()

    

# Selection of choices to be displayed when sending or accepting friend requests
FRIENDSHIP_CHOICES = (
    ('Request Sent', 'Request Sent'),
    ('Request Accepted', 'Request Accepted'),
)

## Friendship Manager Model ##
class FriendshipManager(models.Manager):
    def Received_Requests(self, receiver):
        received_requests = Friendship.objects.filter(receiver=receiver, status='Request Sent')
        return received_requests

# User Friendship Model
class Friendship(models.Model):
    sender = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(UserProfile, on_delete = models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=30, choices=FRIENDSHIP_CHOICES)
    created = models.DateTimeField(auto_now=True)
    updated = models.DateTimeField(auto_now_add=True)

    objects = FriendshipManager()

    def __str__(self):
        return f"{self.sender}-{self.receiver}-{self.status}"
