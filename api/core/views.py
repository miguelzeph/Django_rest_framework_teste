from django.shortcuts import render
from rest_framework import viewsets
from .models import Cliente, Article
from .serializers import ClienteSerializer, ArticleSerializer

# ViewSets define the view behavior.
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

from rest_framework.parsers import JSONParser
from django.http import JsonResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def article_list(request):

    if request.method == 'GET':
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles,many=True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == "POST":
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data,status=201)
        return JsonResponse(serializer.error,status=400)
