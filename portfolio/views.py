from django.shortcuts import render
from .models import Project
def home(request):
  posts = Project.objects.all()
  # posts = [
  #   {
  #     'name':"kashif",
  #     'section':"bscs"
  #   }
  # ]
  return render(request,'portfolio/home.html',{'posts':posts})