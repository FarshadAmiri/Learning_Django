from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import *

class ArticleListView(ListView):
    model = Article
    template_name = 'articles/Article_List.html'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'articles/Article_Detail.html'
    context_object_name = 'article_object'