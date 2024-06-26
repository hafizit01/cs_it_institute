from django.urls import path
from .views import *
urlpatterns = [
    path('', index, name='index'),
    path('course/<slug:slug>/', course_detail, name='course_detail'),
    path('all_course/', all_course, name='all_course'),
    path('category/<slug:slug>/', category_filtering, name='category_filtering'),
    path('teacher/<slug:slug>/', teacher_details, name='teacher_details'),
    path('application-form/', free_application_form, name='free_application_form'),
    path('success/', success, name='success'),
    path('contact/', contact, name='contact_us'),
    path('blog/<slug:slug>/', blog_details, name='blog_details'),

]