from django.shortcuts import render, redirect
from .models import UserPost, Like
from User_Profiles.models import UserProfile
from .forms import UserPostForm, CommentForm
from django.views.generic import DeleteView
from django.contrib import messages
from django.urls import reverse_lazy

def PostsList(request):
    posts = UserPost.objects.all()   
    profile = UserProfile.objects.get(user=request.user)
    
    UserForm = UserPostForm()
    ComForm = CommentForm()
    postadded = False

    profile = UserProfile.objects.get(user=request.user)
     
    if 'SubPostForm' in request.POST:
        print(request.POST)
        UserForm = UserPostForm(request.POST, request.FILES)
        if UserForm.is_valid():
            instance = UserForm.save(commit=False)
            instance.author = profile
            instance.save()
            UserForm = UserPostForm()
            postadded = True

    if 'SubCommentForm' in request.POST:
        ComForm = CommentForm(request.POST)
        if ComForm.is_valid():
            instance = ComForm.save(commit=False)
            instance.user = profile
            instance.post = UserPost.objects.get(id=request.POST.get('post_id'))
            instance.save()
            ComForm = CommentForm()

    context = {
        'posts': posts,
        'profile': profile,
        'UserForm': UserForm,
        'ComForm': ComForm,
        'postadded': postadded,
    }

    return render(request, 'posts/networking.html', context)


def LikeUnlikePost(request):
    user = request.user
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        post_posts = UserPost.objects.get(id=post_id)
        profile = UserProfile.objects.get(user=user)

        if profile in post_posts.liked.all():
            post_posts.liked.remove(profile)
        else:
            post_posts.liked.add(profile)

        like, created = Like.objects.get_or_create(user=profile, post_id=post_id)

        if not created:
            if like.value=='Like':
                like.value='Unlike'
            else:
               like.value='Like'
        else:
            like.value='Like'
            
        post_posts.save()
        like.save()
    
    return redirect('posts:Networking')

class PostDeleteView(DeleteView):
    model = UserPost
    template_name = 'posts/deletepost.html'
    success_url = '/networking/'

    def get_object(self, *args, **kwargs):
        pk = self.kwargs.get('pk')
        post = UserPost.objects.get(pk=pk)
        if not post.author.user == self.request.user:
            messages.warning(self.request, 'You dont have access to delete this post')
        return post
    
