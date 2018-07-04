from django.contrib import admin
from .models import Vacancies, Resume, Cards, CareerTitle, ResumeSection

# Register your models here.

admin.site.register([Vacancies, Resume, Cards, CareerTitle, ResumeSection])
