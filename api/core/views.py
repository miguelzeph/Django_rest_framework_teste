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


from django.http import HttpResponse
@csrf_exempt
def article_detail(request, pk):
    try:
        article = Article.objects.get(pk=pk)
    
    except Article.DoesNotExist:
        return HttpResponse(status=400)
        #return HttpResponse('Deu ruim Paeeee')
    

    if request.method == 'GET':

        serializer = ArticleSerializer(article)
        return JsonResponse(serializer.data)
    
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = ArticleSerializer(article,data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.error,status=400)
    
    elif request.method == "DELETE":
        article.delete()
        return HttpResponse(status = 204)

