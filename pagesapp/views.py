from django.shortcuts import render
from django.views.generic import  TemplateView
from .models import PostHomeCarousel
# Create your views here.

# Post start
def HomeCarouselView(request):
    post = PostHomeCarousel.objects.all()
    return render(request, 'index.html', context={
        'post':post,
    })

# Post end
# Page start
class BasePageView(TemplateView):
    template_name = 'base.html'

class HomePageView(TemplateView):
    template_name = 'index.html'

class AboutPageView(TemplateView):
    template_name = 'about.html'

class BlogPageView(TemplateView):
    template_name = 'blog.html'

class ContactPageView(TemplateView):
    template_name = 'contact.html'

class ProjectPageView(TemplateView):
    template_name = 'project.html'

class ServicePageView(TemplateView):
    template_name = 'service.html'

class SinglePageView(TemplateView):
    template_name = 'single.html'
# Page end
