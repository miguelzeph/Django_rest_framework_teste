from rest_framework import serializers

from .models import Cliente, Article

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente # Chama o Model
        fields = ('id','nome','endereco','idade')

""" 
# Jeito de Fazer no Braço!!! Vamos usar o ModelSerializer em vez do Serializer
class ArticleSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    author = serializers.CharField(max_length=100)
    email = serializers.EmailField(max_length=100)
    date = serializers.DateTimeField()

    def create(self,validated_data):
        return Article.objects.create(validated_data)
    
    def update(self,instance,validated_data):
        instance.title = validated_data.get('title',instance.title)
        instance.author = validated_data.get('author',instance.author)
        instance.email = validated_data.get('email',instance.email)
        instance.date = validated_data.get('date',instance.date)
        instance.save()
        return instance

    # Teste Você mesmo no Shell:
    #Execute no terminal - python manage.py shell
    #Importe as libs
    #>>> from core.models import Article
    #>>> from core.serializers import ArticleSerializer
    #>>> from rest_framework.renderers import JSONRenderer
    #>>> from rest_framework.parsers import JSONParser
    # Crie um objeto no seu Model criado - Article
    #>>> a = Article(title='Titulo do Artigo',author = 'Miguel',email='teste@hotmail.com')
    #>>> a.save()
    # Serialize ele
    #>>> serializer = ArticleSerializer(a)
    # Print...
    #>>> serializer.data
    # Jsonlize ele
    #>>> content = JSONRenderer().render(serializer.data)
    # Print...
    #>>> content"""

# ModelSerializer (melhor)
class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article # Chama o Model
        #fields = "__all__"
        fields =[
            'id',
            'title',
            'email',
            'date',    
        ]