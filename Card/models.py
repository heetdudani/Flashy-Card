from django.db import models

# Create your models here.

class User_id(models.Model):
    dp = models.ImageField(upload_to='dp')
    First_Name = models.CharField()
    Last_Name  = models.CharField()
    Occupation = models.CharField()
    Email = models.EmailField()
    Password = models.CharField()
    location = models.CharField()
    member_since =models.CharField()
    mobile=models.CharField()
    goal = models.CharField()
    
class Course_name_list(models.Model):
    logo = models.ImageField(upload_to='course_logo')
    Course_Title = models.CharField(max_length=255)
    Course_syllabus = models.CharField()
    course_intro = models.CharField()
    Course_description = models.TextField()
    Course_level = models.CharField(max_length=255)
    Course_time = models.CharField(max_length=255)
    
    def __str__(self):
        return self.Course_Title
    
class Modules_list(models.Model):
    course = models.ForeignKey(Course_name_list, on_delete=models.CASCADE, related_name='modules')
    Module_Index = models.IntegerField()
    Module_Title = models.CharField(max_length=255)
    Module_Detail = models.CharField()
    
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['course', 'Module_Title'], name='unique_module_title_per_course'),
            models.UniqueConstraint(fields=['course', 'Module_Index'], name='unique_module_index_per_course'),
        ]
    def __str__(self):
        return f"{self.Module_Title} ({self.course.Course_Title})"
    
class Card(models.Model):
    Card_Index = models.IntegerField()
    course = models.ForeignKey(Course_name_list, on_delete=models.CASCADE, related_name='cards')
    module = models.ForeignKey(Modules_list, on_delete=models.CASCADE, related_name='cards')
    Front = models.TextField()
    Back = models.TextField()