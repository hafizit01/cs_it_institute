from django.db import models
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='CategoryImage/', blank=True, null=True)
    slug = AutoSlugField(populate_from='name', blank=True, null=True)

    class Meta:
        
        verbose_name_plural = 'Categorys'

    def __str__(self):
        return self.name


class Course(models.Model):
    language = (
        ('Bangla', 'Bangla'),
        ('English', 'english')
    )
    image = models.ImageField(upload_to='CourseImage/')
    course_name = models.CharField(max_length=100)
    price = models.PositiveIntegerField(blank=True, null=True)
    discount_price = models.PositiveIntegerField(blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)
    discription = RichTextField()
    enroll_count = models.CharField(max_length=100, blank=True, null=True)
    user_view_count = models.CharField(max_length=500, blank=True, null=True)
    teacher = models.ForeignKey('Teacher', on_delete=models.CASCADE, blank=True, null=True)
    class_duration = models.CharField(max_length=100, blank=True, null=True)
    total_duration = models.CharField(max_length=100, blank=True, null=True)
    total_lecture = models.CharField(max_length=100,blank=True, null=True)
    language = models.CharField(max_length=150, choices=language, blank=True, null=True)
    slug = AutoSlugField(populate_from='course_name', blank=True, null=True)
    class Meta:
        
        verbose_name_plural = 'Courses'

    def __str__(self):
        return self.course_name
    
    def discount_percentage(self):
        if self.price and self.discount_price:
            return (self.price - self.discount_price) / self.price * 100
        return None


class Teacher(models.Model):
    image=models.ImageField(upload_to='TeamImage/')
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=100)
    phone=models.CharField(max_length=14, blank=True, null=True)
    email=models.EmailField(blank=True, null=True)
    address=models.CharField(max_length=200, blank=True, null=True)
    description=RichTextField(blank=True, null=True)
    twitter_link=models.URLField(blank=True, null=True)
    linkedin_link=models.URLField(blank=True, null=True)
    github_link=models.URLField(blank=True, null=True)
    facebook_link=models.URLField(blank=True, null=True)
    slug = AutoSlugField(populate_from='image', blank=True, null=True)


    class Meta:
        verbose_name_plural='Teachers'

    def __str__(self):
        return self.name


class Contact(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField(blank=True, null=True)
    phone=models.CharField(max_length=13, blank=True, null=True)
    subject=models.CharField(max_length=40)
    message=models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name_plural='Contacts'

    def __str__(self):
        return f'{self.name}  {self.subject}'

class Testmonial(models.Model):
    image=models.ImageField(upload_to='TestmonialImage/')
    name=models.CharField(max_length=50)
    designation=models.CharField(max_length=100)
    description=RichTextField(blank=True, null=True)

    class Meta:
        verbose_name_plural='Testmonials'

    def __str__(self):
        return self.name


class Free_course_apply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    phone=models.CharField(max_length=14)
    message=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural='Free_course_applys'

    def __str__(self):
        return self.name


class Blog(models.Model):
    image=models.ImageField(upload_to='BlogImage/')
    #user=models.ForeignKey(User, on_delete=models.CASCADE)
    #user_view_count=models.CharField(max_length=10, blank=True, null=True)
    blog_name=models.CharField(max_length=50)
    blog_date=models.DateField(auto_now=True, blank=True, null=True)
    description=RichTextField(blank=True, null=True)
    slug=AutoSlugField(populate_from='blog_name', blank=True, null=True)

    class Meta:
        verbose_name_plural='blogs'

    def __str__(self):
        return self.blog_name


class Blog_reply(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    website=models.URLField(max_length=100, blank=True, null=True)
    message=models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        verbose_name_plural='Blog_replys'

    def __str__(self):
        return self.name