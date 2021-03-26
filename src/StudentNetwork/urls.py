"""StudentNetwork URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from .views import Register, Login, Logout, Apply, Homepage, Tutoring, PaymentSuccessful, DiscussionBoard, BookMarketplace, Game, AboutUs, ContactUs, Legal, FAQs

urlpatterns = [
    path('admin/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    path('secret/', admin.site.urls),

    path('register/', Register, name='Register'),
    path('login/', Login, name='Login'),
    path('logout/', Logout, name='Logout'),
    path('apply/', Apply, name='Apply'),

    path('', Homepage, name='Homepage'),
    path('tutoring/', Tutoring, name='Tutoring'),
    path('discussionboard/', DiscussionBoard, name='DiscussionBoard'),
    path('bookmarketplace/', BookMarketplace, name='BookMarketplace'),
    path('game/', Game, name='Game'),
    path('aboutus/', AboutUs, name='AboutUs'),
    path('legal/', Legal, name='Legal'),
    path('faqs/', FAQs, name='FAQs'),
    path('contactus/', ContactUs, name='ContactUs'),
    path('profiles/', include('User_Profiles.urls')),
    path('networking/', include('User_Posts.urls')),

    path('paymentsuccessful/', PaymentSuccessful, name='PaymentSuccessful'),

    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('accounts/password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('accounts/reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)