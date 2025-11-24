from django.shortcuts import render,redirect
from django.http import HttpResponse

def page_404(request,exception):
    return render(request, "404.html", status=404)