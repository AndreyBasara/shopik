
from django import views
from django.urls import path
from news.views import news, news_detail

app_name = 'news'

urlpatterns = [
    path('', news, name='news'),
    path('<int:pk>/',news_detail, name='news_detail')
   
]
