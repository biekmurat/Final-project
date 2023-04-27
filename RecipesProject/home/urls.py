

from django.urls import path
from .views import Home
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import render
from django.template import RequestContext

urlpatterns = [
    path('',Home.as_view(),name="home"),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


def handler404(request, *args, **argv):
    response = render('404.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 404
    return response


def handler500(request, *args, **argv):
    response = render('500.html', {},
                                  context_instance=RequestContext(request))
    response.status_code = 500
    return response