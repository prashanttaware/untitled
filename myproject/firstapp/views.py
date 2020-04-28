from django.shortcuts import render
from django.http import HttpResponse
from .models import Allcourses
from django.template import loader


def courses(request):
    ac = Allcourses.objects.all()
    template = loader.get_template('firstapp/course.html')
    context = {
        'ac': ac,
    }

    return HttpResponse(template.render(context, request))


def details(request, course_id):
    return HttpResponse('<h2> These are the details of course_id:' + str(course_id) + '</h2>')
