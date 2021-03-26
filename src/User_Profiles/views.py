from django.shortcuts import render, redirect, get_object_or_404
from .models import UserProfile, Friendship
from User_Posts.models import UserPost
from .forms import UserProfileForm
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User
from django.db.models import Q
from django.conf import settings
from django.contrib.auth.decorators import login_required

@login_required(login_url='/login')
def MyProfile(request):
    profile = UserProfile.objects.get(user=request.user)
    posts = UserPost.objects.all()   

    form = UserProfileForm(request.POST or None, request.FILES or None, instance=profile)
    confirm = False

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            confirm = True

    context = {
        'profile': profile,
        'form': form,
        'confirm': confirm,
        'posts': posts,
    }

    return render(request, 'User_Profiles/userprofile.html', context)

@login_required(login_url='/login')
def Received_Friend_Requests(request):
    profile = UserProfile.objects.get(user=request.user)
    received_requests = Friendship.objects.Received_Requests(profile)

    # Lambda used in order to only display the sender of the requests and not both the sender and receiver
    request_results = list(map(lambda x: x.sender, received_requests))

    context = {'received_requests': request_results}

    return render(request, 'User_Profiles/received_requests.html', context)

def Accept_Friend_Request(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = UserProfile.objects.get(pk=pk)
        receiver = UserProfile.objects.get(user=request.user)
        friendship = get_object_or_404(Friendship, sender=sender, receiver=receiver)
        if friendship.status == 'Request Sent':
            friendship.status = 'Request Accepted'
            friendship.save()
    return redirect("ReceivedRequests")

def Reject_Friend_Request(request):
    if request.method=="POST":
        pk = request.POST.get('profile_pk')
        sender = UserProfile.objects.get(pk=pk)
        receiver = UserProfile.objects.get(user=request.user)
        friendship = get_object_or_404(Friendship, sender=sender, receiver=receiver)
        friendship.delete()
    return redirect("ReceivedRequests")

class Profile_Detail(DetailView):
    model = UserProfile
    template_name = 'User_Profiles/profile_information.html'

    # def get_object(self, slug=None):
    #     slug = self.kwargs.get('slug')
    #     profile = UserProfile.objects.get(slug=slug)
    #     return profile

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = UserProfile.objects.get(user=user)
        friendship_receiver = Friendship.objects.filter(sender=profile)
        friendship_sender = Friendship.objects.filter(receiver=profile)
        friendship_receiver_list = []
        friendship_sender_list = []
        for friendship in friendship_receiver:
            friendship_receiver_list.append(friendship.receiver.user)
        for friendship in friendship_sender:
            friendship_sender_list.append(friendship.sender.user)
        context["friendship_receiver_list"] = friendship_receiver_list
        context["friendship_sender_list"] = friendship_sender_list
        context['posts'] = self.get_object().PostsList

        return context


class Profile_List(ListView):
    model = UserProfile
    template_name = 'User_Profiles/all_profiles.html'

    def get_queryset(self):
        qs = UserProfile.objects.All_Profiles(self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = User.objects.get(username__iexact=self.request.user)
        profile = UserProfile.objects.get(user=user)
        friendship_receiver = Friendship.objects.filter(sender=profile)
        friendship_sender = Friendship.objects.filter(receiver=profile)
        friendship_receiver_list = []
        friendship_sender_list = []
        for friendship in friendship_receiver:
            friendship_receiver_list.append(friendship.receiver.user)
        for friendship in friendship_sender:
            friendship_sender_list.append(friendship.sender.user)
        context["friendship_receiver_list"] = friendship_receiver_list
        context["friendship_sender_list"] = friendship_sender_list

        return context

@login_required(login_url='/login')
def Available_Profiles_To_Add(request):
    user = request.user
    available_profile_list = UserProfile.objects.All_Profiles_Not_Friends_With(user)

    context = {'available_profile_list': available_profile_list}

    return render(request, 'User_Profiles/available_profile_list.html', context)

def Send_Friend_Request(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = UserProfile.objects.get(user=user)
        receiver = UserProfile.objects.get(pk=pk)

        friendship = Friendship.objects.create(sender=sender, receiver=receiver, status="Request Sent")
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("MyProfile")

def Remove_Friend(request):
    if request.method == "POST":
        pk = request.POST.get("profile_pk")
        user = request.user
        sender = UserProfile.objects.get(user=user)
        receiver = UserProfile.objects.get(pk=pk)

        friendship = Friendship.objects.get((Q(sender=sender) & Q(receiver=receiver)) | Q(sender=receiver) & Q(receiver=sender))
        friendship.delete()
        return redirect(request.META.get("HTTP_REFERER"))
    return redirect("MyProfile")