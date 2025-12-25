from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Tweet
from .forms import TweetForm, UserRegistrationForm
from django.shortcuts import get_list_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .forms import SignUpForm
from .forms import CustomUserCreationForm

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # change to your login URL
    else:
        form = SignUpForm()
    return render(request, 'tweet/signup.html', {'form': form})




# Create your views here.
def index(request):
    return render(request, 'index.html')



def home(request):
    return render(request, 'home.html')



@login_required
def my_posts(request):
    # শুধু login user এর tweets
    tweets = Tweet.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tweet/my_posts.html', {'tweets': tweets})

def my_posts(request):
    tweets = Tweet.objects.filter(user=request.user)
    return render(request, 'tweet/my_posts.html', {'tweets': tweets})



def tweet_list(request):
    tweets = Tweet.objects.all().order_by('-created_at')
    return render(
        request,
        'tweet_list.html',
        {'tweets': tweets}
    )
def tweet_list(request):
    query = request.GET.get('q')  # search text
    tweets = Tweet.objects.all()

    if query:
        tweets = tweets.filter(text__icontains=query)

    return render(request, 'tweet_list.html', {
        'tweets': tweets
    })



@login_required
def tweet_create(request):
    if request.method == "POST":
        form = TweetForm(request.POST, request.FILES)
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')  # URL name এখানে দেবে
    else:
        form = TweetForm()

    return render(
        request,
        'tweet_form.html',
        {'form': form}
    )
@login_required
def tweet_edit(request, tweet_id):
    tweet = get_object_or_404(
        Tweet,
        pk=tweet_id,
        user=request.user
    )

    if request.method == "POST":
        form = TweetForm(
            request.POST,
            request.FILES,
            instance=tweet
        )
        if form.is_valid():
            tweet = form.save(commit=False)
            tweet.user = request.user
            tweet.save()
            return redirect('tweet_list')
    else:
        form = TweetForm(instance=tweet)

    return render(
        request,
        'tweet_form.html',
        {'form': form}
    )
@login_required
def tweet_delete(request, tweet_id):
    tweet = get_object_or_404(
        Tweet,
        pk=tweet_id,
        user=request.user
    )
    if request.method == "POST":
        tweet.delete()
        return redirect('tweet_list')
    return render(
        request,
        'tweet_confirm_delete.html',
        {'tweet': tweet}
    )


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('tweet_list')
    else:
        form = UserRegistrationForm() 

    return render(
        request,
        'registration/register.html',
        {'form': form}
    )


def tweet_detail(request, pk):
    tweet = Tweet.objects.get(pk=pk)
    return render(request, 'tweet/tweet_detail.html', {
        'tweet': tweet
    })

def tweet_detail(request, tweet_id):  # note: tweet_id
    tweet = Tweet.objects.get(id=tweet_id)
    return render(request, 'tweet/tweet_detail.html', {
        'tweet': tweet
    })



