from django.shortcuts import render, HttpResponse

# Create your views here.


# index is the view/page
def index(request):
    return HttpResponse("Hello World")
    pass

def about(request):
    return render(request, "about.html")