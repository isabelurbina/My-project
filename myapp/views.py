from django.http import HttpResponse
from .models import Project, task
from django.shortcuts import render, redirect, get_object_or_404
from .forms import CreateNewTask, CreateNewProject
# Create your views here.

def index(request):
	title = 'Django Course!!'
	return render(request,'index.html', {
		'title': title
		})

def hello(request, username):
	print(username)

	return HttpResponse("<h1>Hello %s</h1>" % username)
def about(request): 
	username = 'Isabel'
	return render(request, 'about.html' , {
		'username': username
		})

def projects(request):
	#projects=list(Project.objects.values())
	projects=Project.objects.all()
	return render(request, 'project/projects.html', {
		'projects': projects
		})

def tasks(request):
	#task= Task.objects.get(title=title)
	tasks = task.objects.all()
	return render(request, 'tasks.html', {
		'tasks': tasks
		})	

def create_task(request):
	if request.method == 'GET':
		return render(request, 'create_task.html', {
			'form': CreateNewTask()
			})
	else:
		task.objects.create(title=request.POST['title'],
		description=request.POST['description'], project_id=2)
		return redirect( 'tasks')

def create_project(request):
	if request.method == 'GET':
		return render(request, 'project/create_project.html', {
			'form': CreateNewProject()
		})
	else:
		Project.objects.create(name=request.POST["name"])
		return redirect('projects')

def project_detail(request, id):
	project = get_object_or_404(Project, id=id)
	tasks = task.objects.filter(project_id=id)
	return render(request, 'project/detail.html', {
			'project' : project,
			'tasks' : tasks
		})