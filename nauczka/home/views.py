from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from nauczka.home.models import Course


def home_page(request):
    courses = Course.objects.all()
    return render(request, "html/index.html", {"courses": courses})

def add_online_course(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['course_name'],url=request.POST['course_url'])
        return redirect("/")
    return render(request,"html/add_online_course.html")