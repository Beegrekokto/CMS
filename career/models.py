from django.db import models


class Vacancies(models.Model):
    position = models.CharField(max_length=255)
    link = models.URLField(default='https://merojob.com/')
    number = models.PositiveIntegerField()
    deadline = models.DateField()
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.position

    class Meta:
        verbose_name = "Vacancies"
        verbose_name_plural = "Vacancies"


class Resume(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255)
    phone = models.CharField(max_length=15)
    job_category = models.CharField(max_length=80)
    resume = models.FileField(upload_to='documents/')
    uploaded_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name


class Cards(models.Model):
    title = models.CharField(max_length=100, blank=True)
    title_content = models.TextField()
    detail_content = models.TextField()
    date_added = models.DateField(auto_now=True, auto_now_add=False)
    card_image = models.ImageField(upload_to='career_cards/', default='default.png')
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Cards"
        verbose_name_plural = "Cards"


class CareerTitle(models.Model):
    interesting_at_rs_title = models.CharField(max_length=50)
    position_title = models.CharField(max_length=50)
    map_title = models.CharField(max_length=50)

    def __str__(self):
        return self.interesting_at_rs_title


class ResumeSection(models.Model):
    section_title = models.CharField(max_length=100)
    section_body = models.CharField(max_length=150)
    button_name = models.CharField(max_length=25)

    def __str__(self):
        return self.section_title
