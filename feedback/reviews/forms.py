from django import forms
from .models import Review

#class ReviewForm(forms.Form):
#    user_name = forms.CharField(label = "Your Name", max_length = 100, error_messages = {
#        "required" : "Your name must not be empty",
#        "max_length" : "Please enter a shorter name!"
#    })
#    review_text = forms.CharField(label = "Your Feedback", widget = forms.Textarea, max_length = 200)
#    rating = forms.IntegerField(label = "Your Rating", min_value = 1, max_value = 5)

class ReviewForm(forms.ModelForm): # we can connect this to a Model and Django automatically take
                                    # all the Model fields and infer proper HTML input
    class Meta:
        model = Review # we don't instantiate it, just point at it
        fields = '__all__'
        #exclude = ['owner_comment']
        
        #fields = ['user_name', 'review-text', 'rating']# which fields from the model should be part of the form
        labels = {
            "user_name" : "Your Name",
            "review_text" : "Your Feedback",
            "rating" : "Your Rating"
        }

        error_messages = {
            "user_name" : {
                "required" : "Your name must not be empty!",
                "max_length" : "Please enter a shorter name!"
            }
        }