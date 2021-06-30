from django.db import models
import datetime as dt

# Create your models here.

class Editor(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=30)
  email = models.EmailField()
  phone_number = models.CharField(max_length=10, blank=True)

  def __str__(self): # helpful when returning queries
    return self.first_name
  
  def save_editor(self):
    self.save()

  
  def delete_editor(self):
    self.objects.delete()


  class Meta: # makes specify models-specific options
    ordering = ['first_name'] # this used in formating the order of how it will be saved

class Tags(models.Model):
  name = models.CharField(max_length=30)

  def __str__(self):
    return self.name

class Article(models.Model):
  title = models.CharField(max_length=60)
  post = models.TextField()
  editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
  tags = models.ManyToManyField(Tags)
  pub_date = models.DateTimeField(auto_now_add=True) # this will equate it to true

  @classmethod # todays news
  def todays_news(cls):
    today = dt.date.today()
    print(today)
    news = cls.objects.filter(pub_date__date = today)
    print(news)
    return news
  
  @classmethod # news by date
  def days_news(cls, date):
    news = cls.objects.filter(pub_date__date = date)
    return news
  
