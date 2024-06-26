from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *

# Create your views here.
def index(request):
    
    category = Category.objects.all()
    course = Course.objects.all()
    teacher = Teacher.objects.all()
    testimonial = Testmonial.objects.all()
    blog=Blog.objects.all()
    context = {
        'course':course,
        'teacher':teacher,
        'category':category,
        'testimonial':testimonial,
        'blog':blog,
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

    form=ContactForm(request.POST)
    if request.method=='POST':
        form=ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')

    else:
        form=ContactForm()

    context={
        'teacher':teacher,
        'form':form,
    }
    return render(request, 'main_app/teacher_details.html', context)


def free_application_form(request):
    form=Free_course_applyForm(request.POST)
    if request.method=='POST':
        form=Free_course_applyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form=Free_course_applyForm()

    context={
        'form':form,
    }
    return render(request, 'main_app/free-application-form.html', context)


def success(request):
    return render(request, 'main_app/success.html')


def contact(request):
    form=ContactForm(request.POST, request.FILES)
    if request.method=='POST':
        form=ContactForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=ContactForm()

    context={
        'form':form,
    }

    return render(request, 'main_app/contact_us.html', context)


def blog_details(request,slug):
    blog=get_object_or_404(Blog, slug=slug)
    recent_blog=Blog.objects.all().order_by('-id')[:3]

    form=Blog_replyForm(request.POST, request.FILES)
    if request.method=='POST':
        form=Blog_replyForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form=Blog_replyForm()

    context={
        'blog':blog,
        'recent_blog':recent_blog,
        'form':form,
    }

    return render(request, 'main_app/blog_details.html', context)


def custom_404_view(request,exception):
    return render(request, 'main_app/404.html', status=504)