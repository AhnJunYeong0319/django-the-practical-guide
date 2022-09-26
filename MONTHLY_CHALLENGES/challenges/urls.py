from django.urls import path
from . import views  # import views.py file

urlpatterns = [#path("january", views.january),
               #path("february", views.february),
               path("", views.index, name = "index"), #/challenges/
               path("<int:month>", views.monthly_challenge_by_number),
               path("<str:month>", views.monthly_challenge, name = "month-challenge")] # the text between brackets doesn't, also challenge/whatever will be handled by views.monthly_challenge
        