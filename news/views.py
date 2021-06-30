from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt
from .models import Article

# Create your views here.

def news_of_day(request):
  date = dt.date.today() # gets todays date
  news = Article.todays_news() # get todays articles
  return render(request, 'all-news/today-news.html', {'date':date, 'news':news})

def convert_dates(dates):
  day_number = dt.date.weekday(dates)
  days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]
  day = days[day_number]
  return day

def past_days_news(request, past_date):
  try:
    date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
  except ValueError:
    raise Http404()
    assert  False

  if date == dt.date.today():
    return redirect(news_of_day)
  
  news = Article.days_news(date)
  return render(request, 'all-news/past-news.html', {'date': date, 'news':news})
