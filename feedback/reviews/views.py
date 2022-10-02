from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from .models import Review

from django.views import View

class ReviewView(View): # class-based view
    def get(self, request):
        form = ReviewForm()

        return render(request, "reviews/review.html", {
            "form" : form
        })

    def post(self, request):
        form = ReviewForm(request.POST)

        if form.is_valid(): 
            form.save() 
            return HttpResponseRedirect("/thank-you")

        return render(request, "reviews/review.html", {
            "form" : form
        })
    

'''
def review(request):
    if request.method == "POST":
        #existing_model = Review.objects.get(pk = 1)
        form = ReviewForm(request.POST) # request.POST is a typed data on the form itself / setting 'instance = existing_model' enables update instead of mere saving

        if form.is_valid(): # already pre-defined field in forms.Form
            
            #review = Review(user_name = form.cleaned_data['user_name'],
            #    review_text = form.cleaned_data['review_text'],
            #    rating = form.cleaned_data['rating'])
            #review.save()
            form.save() # this is possible since 'form' is ModelForm, not a mere form
            return HttpResponseRedirect("/thank-you")

    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form" : form
    })
'''
    
def thank_you(request):
    return render(request, "reviews/thank_you.html")