from django.urls import path

from .views import HomePageView, AboutPageView
from users.views import home

urlpatterns = [
    path('', home, name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
   # path('test/', home, name='test')
]
