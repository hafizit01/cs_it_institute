from django.shortcuts import render, get_object_or_404
from .models import *

# Create your views here.
def index(request):
    
    category = Category.objects.all()
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    testimonial = Testmonial.objects.all()
    context = {
        'course':course,
        'teacher':teacher,
        'category':category,
        'testimonial':testimonial,
    }
    return render(request, 'main_app/index.html',context)

def all_course(request):
    course = Course.objects.all()
    context = {
        'course':course,
    }
    return render(request, 'main_app/our-courses.html',context)

def course_detail(request,slug):
    course = get_object_or_404(Course, slug=slug)
    context = {
        'course':course
    }
    return render(request, 'main_app/course_detail.html', context)

def category_filtering(request, slug):
    category = get_object_or_404(Category, slug=slug)
    products = Course.objects.filter(category=category)

    context = {
        'category': category,
        'products': products,
    }
    return render(request, 'main_app/category.html', context)


def teacher_details(request,slug):
    teacher = get_object_or_404(Teacher, slug=slug)
    context={
        'teacher':teacher
    }
    return render(request, 'main_app/teacher_details.html', context)

def free_application_form(request):
    return render(request, 'main_app/free-application-form.html')

def success(request):
    return render(request, 'main_app/success.html')

def custom_404_view(request,exception):
    return render(request, 'main_app/404.html', status=504)