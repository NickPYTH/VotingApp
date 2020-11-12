from django.shortcuts import render

# Create your views here.

def vote_list(request):
    return render(request, "index.html")
