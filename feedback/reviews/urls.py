from django.urls import path
from . import views
urlpatterns = [
    #path("", views.review),
    path("", views.ReviewView.as_view()), # as_view() is an attribute in View class object (from django.views import View)
                                          # and we can use it with ReviewView class object since it is extended from View class.
    path("thank-you", views.ThankYouView.as_view()),
    path("reviews", views.ReviewsListView.as_view()),
    path("reviews/<int:pk>", views.SingleReviewView.as_view()) # 'id' identifier goes to kwargs in views.py
]