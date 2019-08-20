from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date =dt.date.today()
    
    return render(request, 'all-news/today-news.html',{"date":date,})
#presents news from past days
def past_days_news(request,past_date):

    try:
    #converts data from the string url
        date = dt.datetime.strptime(past_date,'%y-%m-%d').date()

    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-news/past-news.html', {"date": date})