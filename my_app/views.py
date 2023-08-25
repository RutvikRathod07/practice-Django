from django.shortcuts import render
from django.http import HttpResponse

stu_list = [
    {
        'name': "rutvik",
        'age': 21,
        'roll_no': 44,
        'image_no': 1
    }, {
        'name': "arpit",
        'age': 18,
        'roll_no': 42,
        'image_no': 2
    }, {
        'name': "nisarg",
        'age': 22,
        'roll_no': 54,
        'image_no': 3
    }
]


# Create your views here.
def show_home_page(request):
    stu_dict = {'stu_list': stu_list}
    return render(request, 'home.html', stu_dict)


def add(request):
    num1 = int(request.GET['val1'])
    num2 = int(request.GET['val2'])
    res = num1 + num2
    return render(request, 'result.html', {'result': res})


def about_page(request):
    return HttpResponse("this is about page")


def info_page(request):
    return render(request, 'info.html', {'name': 'Nisarg'})


def service_page(request):
    return HttpResponse("this is service page")
