from django.shortcuts import render

def hello_world(request):
    context = {
        'app_name': 'MeuApp',
    }
    return render(request, 'index.html', context)
