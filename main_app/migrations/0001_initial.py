# Generated by Django 4.2.13 on 2024-06-02 18:51

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='CourseImage/')),
                ('course_name', models.CharField(max_length=100)),
                ('price', models.PositiveIntegerField(blank=True, null=True)),
                ('discount_price', models.PositiveIntegerField(blank=True, null=True)),
                ('discription', ckeditor.fields.RichTextField()),
                ('enroll_count', models.CharField(blank=True, max_length=100, null=True)),
                ('user_view_count', models.CharField(blank=True, max_length=500, null=True)),
                ('class_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('total_duration', models.CharField(blank=True, max_length=100, null=True)),
                ('total_lechture', models.CharField(blank=True, max_length=100, null=True)),
                ('language', models.CharField(blank=True, choices=[('Bangla', 'Bangla'), ('English', 'english')], max_length=150, null=True)),
            ],
            options={
                'verbose_name_plural': 'Courses',
            },
        ),
    ]
