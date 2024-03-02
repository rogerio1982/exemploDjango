from django.shortcuts import render

# Create your views here.
# Create your views here.
#def home(request):
#    return render(request, 'index.html')

from django.shortcuts import render
from loja.models import produto

def home(request):
    project = produto.objects.all()
    context = {
        'projects': project
    }
    return render(request, 'index.html', context)