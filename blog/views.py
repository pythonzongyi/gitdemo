from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article

def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles': articles})

