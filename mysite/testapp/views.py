from django.shortcuts import render
from .models import Rubric


def testapp(request):
    return render(request, "testapp/testapp.html", {'rubrics': Rubric.objects.all()})


def get_rubric(request):
    pass
