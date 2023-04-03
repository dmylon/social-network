from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from datetime import datetime
import json
from django.core.paginator import Paginator

from .models import User, Profile, Post


def index(request):
    if request.user.is_authenticated:

        if "page" not in request.GET:
            page_num = 1
        else:
            page_num = request.GET["page"]

        posts = Post.objects.all()
        p = Paginator(posts, 10)
        
        if int(page_num) > p.num_pages:
            return HttpResponseRedirect(reverse("index")) 
        

        return render(request, "network/index.html",{
            "page_num" : page_num
        })
    else:
        return HttpResponseRedirect(reverse("login"))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            Profile.objects.create(user=user)
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    elif request.user.is_authenticated:
        logout(request)
        return render(request, "network/register.html")
    else:
        return render(request, "network/register.html")

@csrf_exempt
@login_required
def newPost(request):
    if request.method != "POST":
        return JsonResponse({"error": "Invalid method"}, status=400)
    
    post_receiver = json.loads(request.body)
    content = post_receiver.get("content","")
    owner = Profile.objects.get(user=request.user)

    Post.objects.create(owner=owner, content=content, date=datetime.now())

    return JsonResponse({"message": "Posted Successfully"})


def loadPosts(request,info):

    if request.method != "GET":
        return JsonResponse({"error": "Invalid method"}, status=400)
    
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    if info == "all":
        posts = Post.objects.all()
    
    elif info.isnumeric():
        user = User.objects.get(id=info)
        posts = Post.objects.filter(owner=Profile.objects.get(user=user))

    elif info == "following":
        followers = Profile.objects.get(user=request.user).following.all()
        followers_profiles = Profile.objects.filter(user__in=followers)
        posts = Post.objects.filter(owner__in=followers_profiles)

    if "page" in request.GET:
        page = request.GET["page"]
    else:
        page = 1
    posts = posts.order_by("-date").all()
    p = Paginator(posts, 10)

    return JsonResponse([{
        "id": post.id,
        "owner": post.owner.user.username,
        "content": post.content,
        "date": post.date.strftime("%B %d, %Y, %H:%M %p"),
        "likes": post.liked_by.count(),
        "liked": (post.liked_by.filter(user=request.user).count() != 0),
        "next": p.num_pages
    } for post in p.page(page)], safe=False)



def viewProfile(request, username):

    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse("login"))

    user = User.objects.get(username=username)
    profile = Profile.objects.get(user=user)

    if user.followers.filter(user=request.user).count() == 0:
        follow = "Follow"
    else:
        follow = "Unfollow"

    if "page" not in request.GET:
        page_num = 1
    else:
        page_num = request.GET["page"]
        

    return render(request, "network/profile.html",{
        "profile": profile,
        "profile_user": user,
        "username":username,
        "follow_status": follow,
        "page_num": page_num
    })


def viewFollowing(request):
    followers = Profile.objects.get(user=request.user).following.all()
    print(followers.count())
    if followers.count() == 0:
        noPosts = True
    else:
        noPosts = False

    if "page" not in request.GET:
        page_num = 1
    else:
        page_num = request.GET["page"]

    followers = Profile.objects.get(user=request.user).following.all()
    followers_profiles = Profile.objects.filter(user__in=followers)
    posts = Post.objects.filter(owner__in=followers_profiles)
    p = Paginator(posts, 10)
        
    if int(page_num) > p.num_pages:
            return HttpResponseRedirect(reverse("viewFollowing")) 

    return render(request, "network/following.html",{
        "noPosts": noPosts,
        "page_num" : page_num
    })


@csrf_exempt
@login_required
def loadPostById(request, id):
   
    if request.method != "PUT":
        return HttpResponse(400)

    if Post.objects.filter(id=id).count() == 0:
        return HttpResponse(400)

    post = Post.objects.get(id=id)
    post_receiver = json.loads(request.body)
    
    if (post_receiver.get("content") is not None):
        post.content = post_receiver["content"]
        post.date = datetime.now()
    
    if (post_receiver.get("username") is not None):
        unlike = post_receiver["unlike"]
        user = User.objects.get(username=post_receiver["username"])
        profile = Profile.objects.get(user=user)

        if unlike:
            post.liked_by.remove(profile)
        else:
            post.liked_by.add(profile)
    
    post.save()

    return HttpResponse(204)


@csrf_exempt
@login_required
def followUser(request):

    if request.method != "PUT":
        return HttpResponse(400)

    user_receiver = json.loads(request.body)
    
    profile = Profile.objects.get(user=request.user)
    user = User.objects.get(username=user_receiver["username"])
    follow = user_receiver["follow"]

    if follow:
        profile.following.add(user)
    else:
        profile.following.remove(user)
    
    profile.save()

    return HttpResponse(204)

