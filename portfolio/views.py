from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    return render(request, 'portfolio/home.html')

def download_cv(request):
    file_path = os.path.join(settings.BASE_DIR, 'portfolio', 'static', 'portfolio_files', 'YuanyuanLu_AI&SofwareDeveloper.pdf')
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='YuanyuanLu_AI&SofwareDeveloper.pdf')
    else:
        # Handle file not found error
        return render(request, '404.html') # You might want to create a custom 404 page

def about(request):
    return render(request, 'portfolio/about.html')

def contact(request):
    return render(request, 'portfolio/contact.html')

def education(request):
    return render(request, 'portfolio/education.html')

def experience(request):
    return render(request, 'portfolio/experience.html')

from .models import ProjectGroup

def projects(request): 
    project_groups = ProjectGroup.objects.prefetch_related(
        'projects__technologies', 
        'projects__images'
    ).all()
    return render(request, 'portfolio/projects.html', {'project_groups': project_groups})

def hobbies(request):
    return render(request, 'portfolio/hobbies.html')