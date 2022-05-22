from django.conf.urls import url, include
from django.contrib import admin

from .import views

urlpatterns = [
    url('^$', views.welcome, name  = 'welcome'),
    url('^admin$', admin.site.urls),
    url('^news/', include('news.urls'))
    ]


# from django.conf.urls import url,include
# from django.contrib import admin

# urlpatterns=[
#     url('^admin$', admin.site.urls),
#     url('^news/', include('news.urls'))
# ]
