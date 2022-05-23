from django.conf.urls import url
from .import views

urlpatterns = [
    url('^news.today$', views.welcome, name  = 'welcome')
    # url(r'^today/', views.welcome, name = 'welcome')
    ]


