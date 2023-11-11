from .models import Project
from django.shortcuts import render, get_object_or_404


def home(request):
    projects = Project.objects.all()     # pega todos os objetos do banco de dados!
    return render(request, 'portfolio/home_backup.html', {'projects': projects})



def detail2(request, proj_id):

    project = get_object_or_404(Project, pk=proj_id)

    return render(request, 'portfolio/detail2.html', {'project': project})

# Projects
# def projeto1(request):
#     return render(request, 'portfolio/projeto1.html')

# def projeto2(request):
#     return render(request, 'portfolio/projeto2.html')

# def projeto3(request):
#     return render(request, 'portfolio/projeto3.html')

# def projeto4(request):
#     return render(request, 'portfolio/projeto4.html')


