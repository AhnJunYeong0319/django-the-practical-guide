from django.shortcuts import render
from datetime import date

# Create your views here.

all_posts = [
    {
        "slug" : "discharged-from-the-army",
        "image" : "discharged_from_the_army.jpg",
        "author" : "Jun",
        "date" : date(2022, 9, 21),
        "title" : "Discharge",
        "excerpt" : "I've recently discharged from the army finishing my service for the past one and a half years. I served in Busan, so at the last day I went on a trip with some of my best friends!",
        "content" : """
        discharge

        asd

        asdfkl;
        """
    },
    {
        "slug" : "stable-diffusion",
        "image" : "stable_diffusion.jpg",
        "author" : "Jun",
        "date" : date(2022, 9, 23),
        "title" : "Stable Diffusion",
        "excerpt" : "I've recently discharged from the army finishing my service for the past one and a half years. I served in Busan, so at the last day I went on a trip with some of my best friends!",
        "content" : """
        stable-diffusion
        """
    },
    {
        "slug" : "traveling-to-Busan",
        "image" : "traveling_busan.jpg",
        "author" : "Jun",
        "date" : date(2022, 9, 21),
        "title" : "Traveling to Busan",
        "excerpt" : "I've recently discharged from the army finishing my service for the past one and a half years. I served in Busan, so at the last day I went on a trip with some of my best friends!",
        "content" : """
        traveling to Busan
        """
    }
]

def get_date(post):
    return post['date']

def starting_page(request):
    sorted_posts = sorted(all_posts, key = get_date)
    latest_posts = sorted_posts[-3:]
    return render(request, "blog/index.html", {
        "posts" : latest_posts
    })

def posts(request):
    return render(request, "blog/all-posts.html", {
        "all_posts" : all_posts
    })

def post_detail(request, slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request, "blog/post-detail.html", {
        "post" : identified_post
    })