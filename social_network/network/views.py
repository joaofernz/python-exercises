from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import PostForm
from .models import Post, Profile


class HomeFeedView(ListView):
    model = Post
    template_name = 'network/home.html'
    context_object_name = 'posts'
    ordering = ['-created_at']


class UserProfileView(DetailView):
    model = Profile
    template_name = 'network/profile.html'
    context_object_name = 'profile'


class CreatePostView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = 'network/create_post.html'
    fields = ['content', 'image']
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')  # Redirect logged-in users to their profile
    else:
        return render(request, 'home.html')


@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def create_post(request):
    if request.method == 'POST':
        # Process form data and save post
        ...
        return redirect('home')  # Redirect to home page after post creation
    else:
        return render(request, 'create_post.html')


def welcome(request):
    return render(request, 'welcome.html')


@login_required
def feed(request):
    posts = Post.objects.all()
    return render(request, 'feed.html', {'posts': posts})


@login_required
def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('feed')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form': form})


def profile(request):
    return render(request, 'network/profile.html')
