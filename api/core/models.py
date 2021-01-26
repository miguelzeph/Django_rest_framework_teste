from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length = 50)
    endereco = models.CharField(max_length=50)
    idade = models.IntegerField()

    def __str__(self):
        return self.nome


class Article(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title