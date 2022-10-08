from django.shortcuts import render
from .models import feedbackdata
from .forms import feedbackform
from django.http.response import HttpResponse
import datetime as dt

date1 = dt.datetime.now()

def feedback_view(request):
    if request.method =="POST":
        form =feedbackform(request.POST)
        if form.is_valid():
            name1 = request.POST.get('name')
            rating1 = request.POST.get('rating')
            feedback1 = request.POST.get('feedback')

            data = feedbackdata(
                name=name1,
                date=date1,
                rating=rating1,
                feedback=feedback1
            )
            data.save()
            feedb = feedbackdata.objects.all()
            form=feedbackform()
            return render(request,'feedbackdata.html',{'form':form , 'feedb':feedb})

    else:
        form = feedbackform()
        feedb  = feedbackdata.objects.all()
        return render(request,'feedbackdata.html',{'form':form , 'feedb':feedb})

