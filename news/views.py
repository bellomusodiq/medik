from django.shortcuts import render
from .models import Article
from .serializers import ArticleSerializer
from rest_framework.viewsets import ModelViewSet
# Create your views here.


class ArticleViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
