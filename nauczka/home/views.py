from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from nauczka.home.models import Course, Note


def home_page(request):
    courses = Course.objects.all()
    return render(request, "index.html", {"courses": courses})

def add_online_course(request):
    if request.method == 'POST':
        Course.objects.create(name=request.POST['course_name'],url=request.POST['course_url'])
        return redirect("/")
    return render(request,"add_online_course.html")

def get_course_details(request,course_id):
    course = Course.objects.get(pk=course_id)
    notes = Note.objects.filter(course=course)
    return render(request,"get_course_details.html", { "id": course.id,"course_name" : course.name, "course_site" : course.url, "notes": notes})

def add_note_to_course(request,course_id):
    course = Course.objects.get(pk=course_id)
    time_spent_in_mins = request.POST['time_spent']
    description = request.POST['description']

    Note.objects.create(time_spent=time_spent_in_mins,description=description,course=course)

    return redirect("/courses/%d/" % (int(course_id),))