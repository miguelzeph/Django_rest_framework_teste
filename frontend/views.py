from django.shortcuts import render,redirect

# Meus arquivos
from api.models import Task, Client


# GET (read)
def home_page(request):
    task = Task.objects.all()
    client = Client.objects.all()

    data = {
        'task': task,
        'client':client
    }
    return render(request,'home.html', data)


# --------------------- TASK ---------------------------

#########################################################
############ CRUD - Creat/READ/UPDATE/DELETE ############
#########################################################
# POST (create)
def create_model_task(request):

    # Tive que fazer isso, pq a Tag html de checkbox
    # não tem opição de True/False
    # tive que colocar os try/except... pq quando está uncheched a box
    # ele dá um erro... exemplo, checked -> retorna 'on' dai eu mudo pra True
    # unchecked -> retorna um dicionário ou algo do tipo... dai eu forço ele ser false
    try:
        if request.POST['completed'] == 'on':
            completed = True
        else:
            completed = False
    except:
        completed = False
    #################################################


    Task.objects.create(
        title = request.POST['title'],
        completed = completed
    )

    return redirect('home')

# PUT (update)
"""
Fiz no Braço esse, coloquei pra ir direto pra página ./api/task/id
"""

# DELETE
def delete_model_task(request, pk):
	task = Task.objects.get(id=pk)
	task.delete()

	return redirect('home')


#########################################################
#########################################################

#------------------------ CLIENT----------------------------

# POST (create)
def create_model_client(request):

    Client.objects.create(
        name = request.POST['name'],
        age = request.POST['age']
    )

    return redirect('home')

# PUT (update)
"""
Fiz no Braço esse, coloquei pra ir direto pra página ./api/client/id
"""

# DELETE
def delete_model_client(request, pk):
	client = Client.objects.get(id=pk)
	client.delete()

	return redirect('home')
