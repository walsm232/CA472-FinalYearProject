from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.mail import EmailMessage
from .forms import CreateUserForm, ApplicationForm
from django.conf import settings
from User_Profiles.models import UserProfile
from django.contrib.auth.models import User

import stripe

def Register(request):
    ## Check for POST method, if form is valid then save and redirect to login
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Registration successful. An account has been created for ' + user)
            return redirect('Login')

    context = {
        'form': form
    }

    return render(request, 'main/register.html', context)


def Login(request):
    ## Checks for username and password in database. If user is found: Log in the user and redirect to Networking page
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('posts:Networking')
        else:
            messages.info(request, 'The Username or Password entered is incorrect')

    context = {}

    return render(request, 'main/login.html', context)

def Logout(request):
    logout(request)
    return redirect('Homepage')


def Apply(request):
    ## Email Sender for Tutor Application
    if request.method == 'POST':
        name = request.POST['name']
        message = request.POST['message']
        message_email = request.POST['message-email']
        CV = request.POST['CV']

        email = EmailMessage(
            name + ' - Tutor Application Form',
            message,
            message_email,
            ['studentnetwork.ire@gmail.com'],
        )
        email.attach(CV, CV, 'application/pdf')
        email.send()

        return render(request, 'main/apply.html')
    else:
        return render(request, 'main/apply.html')
  

def Homepage(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/homepage.html', context)



@login_required(login_url='/login')
def Tutoring(request):
    profiles = UserProfile.objects.all()
    
    ## Stripe Checkout Session Setup
    ## Stripe API Documentation used as a reference when building this checkout
    ## https://stripe.com/docs/api
    
    stripe.api_key = settings.STRIPE_PRIVATE_KEY

    session = stripe.checkout.Session.create(
        payment_method_types=['card'],
        line_items=[{
            'price': 'price_1IXRj1IqhFLgIZBMJzn60Jb9',
            'quantity': 1,
        }],
        mode='payment',
        success_url='http://127.0.0.1:8000/paymentsuccessful',
        cancel_url='http://127.0.0.1:8000/tutoring/',
    )

    context = {
        'session_id' : session.id,
        'stripe_public_key' : settings.STRIPE_PUBLIC_KEY,
        'profiles': profiles,
    }

    return render(request, 'main/tutoring.html', context)


@login_required(login_url='/login')
def PaymentSuccessful(request):
    return render(request, 'main/paymentsuccessful.html')


@login_required(login_url='/login')
def DiscussionBoard(request):
    user = request.user

    context = { 
        'user': user,
    }
    return render(request, 'main/discussionboard.html', context)


@login_required(login_url='/login')
def BookMarketplace(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/bookmarketplace.html', context)


def Game(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/game.html', context)


def AboutUs(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/aboutus.html', context)


def Legal(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/legal.html', context)


def FAQs(request):
    user = request.user

    context = {
        'user': user,
    }
    return render(request, 'main/faqs.html', context)


def ContactUs(request):
    ## Email Sender for Contact Us
    if request.method == 'POST':
        subject = request.POST['subject']
        message = request.POST['message']
        message_email = request.POST['message-email']

        email = EmailMessage(
            subject,
            message,
            message_email,
            ['studentnetwork.ire@gmail.com'],
        )
        email.send()

        return render(request, 'main/contactus.html')
    else:
        return render(request, 'main/contactus.html')