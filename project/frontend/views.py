from django.shortcuts import render

# Meus arquivos
from api.models import Task, Client


#########################################################
############ CRUD - Creat/READ/UPDATE/DELETE ############
#########################################################
# GET (read)
def home_page(request):
    task = Task.objects.all()
    client = Client.objects.all()

    data = {
        'task': task,
        'client':client
    }
    return render(request,'home.html', data)
"""
# POST (create)
def create_form(request):

    #Cria OBjeto no DB
    form = Task(request.POST)
    if form.is_valid():
        form.save()
    return render(request,'home.html')
"""
# PUT (update)

# DELETE

#########################################################
#########################################################