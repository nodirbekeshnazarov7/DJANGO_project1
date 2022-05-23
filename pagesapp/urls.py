from .views import BasePageView, HomePageView, AboutPageView, ContactPageView, BlogPageView, ProjectPageView, ServicePageView, SinglePageView, HomeCarouselView
from django.urls import path
urlpatterns = [
    path('home', HomeCarouselView, name='carousel'),
    path('', BasePageView.as_view(), name='base'),
    path('home', HomePageView.as_view(),name='home'),
    path('about', AboutPageView.as_view(), name='about'),
    path('contact', ContactPageView.as_view(), name='contact'),
    path('blog', BlogPageView.as_view(), name='blog'),
    path('project', ProjectPageView.as_view(), name='project'),
    path('services', ServicePageView.as_view(), name='services'),
    path('single', SinglePageView.as_view(), name='single')
]