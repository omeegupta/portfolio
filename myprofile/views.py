from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
# Create your views here.

def home(request):
    category = Category.objects.filter(status=1)
    project = Project.objects.filter(status=1)
    data = {'category': category, 'project':project}
    return render(request, 'index.html', data)
    
def getproject(request):
    if request.method == "POST":
        
        id = request.POST['id']
        project = Project.objects.get(id=id)
        if project:
            
            image = json.dumps(str(project.image))
            data = {'status':'success', 'title': project.title, 'project_info': project.project_info, 'image':image, 'client_name': project.client_name, 'industry': project.industry, 'technology': project.technology, 'link_title_name': project.link_title_name, 'link': project.link}
        else:
            data = {'status':'fail'}
    return JsonResponse(data)
    
def contactus(request):
    if request.method == "POST":
        
        name = request.POST['name']
        email = request.POST['email']
        msg = request.POST['msg']
        
        contact = Contact.objects.create(name=name, email=email, msg=msg)
        contact.save()
        
        
        data = {'status':'success'}
    return JsonResponse(data)
