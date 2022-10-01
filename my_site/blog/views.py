from django.shortcuts import render, get_object_or_404
#from datetime import date
from .models import Post

# Create your views here.

#all_posts = [
    #{
    #    "slug" : "discharged-from-the-army",
    #    "image" : "discharged_from_the_army.jpg",
    #    "author" : "Jun",
    #    "date" : date(2022, 9, 21),
    #    "title" : "Discharge",
    #    "excerpt" : "I've recently discharged from the army finishing my service for the past one and a half years. I served in Busan, so at the last day I went on a trip with some of my best friends!",
    #    "content" : """
    #    discharge
    #
    #    asd
    #
    #    asdfkl;
    #    """
    #},

#]

#def get_date(post):
#    return post['date']

def starting_page(request):
    latest_posts = Post.objects.all().order_by("-date")[:3]
    #sorted_posts = sorted(all_posts, key = get_date)
    #latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    all_posts = Post.objects.all().order_by("-date")
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_detail(request, slug):
    #identified_post = next(post for post in all_posts if post['slug'] == slug)
    identified_post = get_object_or_404(Post, slug = slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post,
        "post_tags" : identified_post.tags.all()
    })