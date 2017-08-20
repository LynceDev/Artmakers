from django.shortcuts import render
from django.http import HttpResponse
from .models import Gallery

def Display_Gallery(request):
    queryset = Gallery.objects.all()
    context = {
        "gallerys": queryset,
    }

    return render(request, "homepage.html", context)

def Display_About_Page(request):
    queryset = Gallery.objects.all()
    profile = {
        "gallerys": queryset,
    }

    return render(request, "about.html", profile)

def Display_Contact_Page(request):

    return render(request, "contact.html")

def Display_Details_Page(request, gallery_id):
    try:
        gallery = Gallery.objects.get(pk=gallery_id)
    except Gallery.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request, "details.html", {'gallery': gallery})


# Create your views here.
