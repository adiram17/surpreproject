from . import views
from django.conf.urls import url

urlpatterns = [

    url(r'^$', views.home, name='home'),
    url(r'^change_password$', views.changePassword, name='change_password'),
    url(r'^score$', views.score, name='score'),
    url(r'^about$', views.about, name='about'),
    url(r'^scoreattribute$', views.scoreattribute, name='scoreattribute'),
    url(r'^scorescale$', views.scorescale, name='scorescale'),
    url(r'^scorelevel$', views.scorelevel, name='scorelevel'),
    url(r'^scorehistory$', views.scorehistory, name='scorehistory'),
    url(r'^test$', views.test, name='test'),
    url(r'^getmessage$', views.getmessage, name='getmessage'),
    url(r'^scorepost$', views.scorepost, name='scorepost'),

    url(r'^report/generatescoregraph', views.generateScoreGraph, name='generate_score_graph'),
    
]

