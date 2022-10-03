from django.shortcuts import render
from django.http import HttpResponseRedirect
# Create your views here.
from .forms import ReviewForm
from .models import Review

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.views.generic.edit import CreateView # specialized one of FormView that automatically save data for us

#class ReviewView(View): # class-based view
#    def get(self, request): # called when the request type is GET
#        form = ReviewForm()

#        return render(request, "reviews/review.html", {
#            "form" : form
#        })

#    def post(self, request): # called when the request type is POST
#        form = ReviewForm(request.POST)

#        if form.is_valid(): 
#            form.save() 
#            return HttpResponseRedirect("/thank-you")

#        return render(request, "reviews/review.html", {
#            "form" : form
#        })
    

#class ReviewView(FormView): 

#    form_class = ReviewForm
#    template_name = "reviews/review.html"
#    success_url = "/thank-you"

#    def form_valid(self, form): # form parameater is passed only if the form is validated.
#        form.save()
#        return super().form_valid(form)

#    # get method is now automatically constructed by Django

class ReviewView(CreateView): # you don't even need to create your own review form
                              # since CreateView creates form from the pointed model then save data that came from it at once.

    model = Review
    form_class = ReviewForm # but you have to set this option (with ReviewForm defined) when you want to customize more than 'fields'.
    #fields = "__all__" # if you are to set only fields, don't have to define ReviewForm class.
    template_name = "reviews/review.html"
    success_url = "/thank-you"


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
#class ThankYouView(View): # class-based view
#    def get(self, request):
#        return render(request, "reviews/thank_you.html")

class ThankYouView(TemplateView): # specialized view for rendering templates
    template_name = "reviews/thank_you.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["message"] = "This works!"
        return context
    

#class ReviewsListView(TemplateView):
#    template_name = "reviews/review_list.html"

#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        reviews = Review.objects.all()
#        context['reviews'] = reviews
#        return context

class ReviewsListView(ListView):
    template_name = "reviews/review_list.html"
    model = Review # as usual, just pointing at the model, not instantiating it
    context_object_name = "reviews" # if you don't set this option, automatically set to "object_list"

    def get_queryset(self):
        base_query = super().get_queryset()
        data = base_query.filter(rating__gt = 4)
        return data

    # ListView automatically passes the data fetched from model as context to the template above
    # Also automatically stored in 'object_list' variable, since we do not specified it


#class SingleReviewView(TemplateView):
#    template_name = "reviews/single_review.html"
#
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        review_id = kwargs["id"]
#        selected_review = Review.objects.get(pk = review_id)
#
#        context['review'] = selected_review
#        return context

class SingleReviewView(DetailView):

    template_name = "reviews/single_review.html"
    model = Review

    # in urls.py, we passed <int:pk> to this function. So Django automatically find the single piece of data
    # correspondes to that key and exposes to our template, although single_review file is trying to use a data from
    # review variable, which is not defined here.

    # So if you still want to touch some fields of automatically fetched data,
    # use 'object' variable name. It is created by Django.
    