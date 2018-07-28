from django.http import HttpResponse
from django.shortcuts import render

from blog.models import Article

def index(request):
    articles = Article.objects.all()
    return render(request,'index.html',{'articles': articles})


def page(request,article_id):
    article = Article.objects.get(pk=article_id)

    return render(request,'page.html',{'article':article})


def edit_page(request,article_id):
    if str(article_id) == '0':
        return render(request,'edit_page.html')
    article = Article.objects.get(pk=article_id)
    return render(request,'edit_page.html',{'article':article})



def edit_action(request):
    title = request.POST.get('title', 'Title')
    content = request.POST.get('content', 'Content')
    article_id = request.POST.get('article_id', '0')

    if str(article_id) == '0':
        Article.objects.create(title=title,content=content)
        articles = Article.objects.all()

        return render(request,'index.html',{'articles':articles})
    article = Article.objects.get(pk=article_id)
    article.title = title
    article.content = content
    article.save()
    return render(request,'page.html',{'article':article})
