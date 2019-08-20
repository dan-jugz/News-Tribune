from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def news_of_day(request):
    date =dt.date.today()
    
    return render(request, 'all-news/today-news.html',{"date":date,})

def past_days_news(request,past_date):
    #converts data from the string url
    date = dt.datetime.strptime(past_date,'%y-%m-%d').date()

    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()
        assert False

    day = convert_dates(date)
    html =f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)