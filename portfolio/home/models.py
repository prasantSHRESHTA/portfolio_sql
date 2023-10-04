from django.db import models

GRADE_CHOICES = (
    ('CGPA', 'CGPA'),
    ('PERCENTAGE', '%')
)


# Create your models here.
class projects(models.Model):
    p_id = models.AutoField(primary_key=True)
    project_title = models.CharField(max_length=100)
    skills_used = models.CharField(max_length=100)
    description = models.TextField()
    github_link = models.URLField(blank=True)

    def __str__(self):
        return self.project_title


class resume(models.Model):
    resume = models.FileField(upload_to="resume/", default=None)


class edu(models.Model):
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=50)
    field_of_study = models.CharField(max_length=50, blank=True)
    start_date = models.DateField(blank=True,null=True)
    end_date = models.DateField()
    grade_choice = models.CharField(max_length=10, choices=GRADE_CHOICES)
    grade = models.FloatField()
    degree_link = models.FileField(upload_to="degree", default=None, null=True,blank=True)

    def __str__(self):
        return self.degree

    def start_year(self):
        return self.start_date.strftime('%Y')

    def end_year(self):
        return self.end_date.strftime('%Y')


class exp(models.Model):
    company = models.CharField(max_length=50)
    Title = models.CharField(max_length=60)
    start_date = models.DateField()
    still_working = models.BooleanField(default=False)
    end_date = models.DateField(blank=True)
    total_exp_in_months = models.IntegerField()
    desc = models.TextField()

    def __str__(self):
        return self.company
