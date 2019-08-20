from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return HttpResponse('welcome to the moringa tribune')

def news_of_day(request):
    date =dt.date.today()
    # FUNCTION TO CONVERT DATE OBJECT TO FIND EXACT DAY
    day = convert_dates(date)
    html = f'''
            <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
            </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    #function that gets weekday no for the date
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

def past_days_news(request,past_date):
    #converts data from the string url
    date = dt.datetime.strptime(past_date,'%y-%m-%d').date()

    except ValueError:
        #raise 404 error when valueError is thrown
        raise Http404()

    day = convert_dates(date)
    html =f'''
        <html>
            <body>
                <h1>News for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)