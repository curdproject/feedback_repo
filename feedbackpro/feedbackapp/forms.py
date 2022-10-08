from django import forms

class feedbackform(forms.Form):

    name = forms.CharField(
        label= "Enter your name",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your name'
            }
        )
    )

    rating = forms.IntegerField(
        label="Enter you rating",
        widget=forms.NumberInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter Your rating'
            }
        )
    )

    feedback = forms.CharField(
        label="Enter your feedback",
        widget=forms.TextInput(
            attrs={
                'class':'form-control',
                'placeholder':'Enter your feedback'
            }
        )
    )