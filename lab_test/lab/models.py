from django.db import models

class Group(models.Model):
    name = models.CharField(max_length=100)
    curator = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Club(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    clubs = models.ManyToManyField(Club, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to='students_photos/', blank=True, null=True)

    
    class Meta:
        verbose_name = "Student"
        verbose_name_plural = "Students"
    def __str__(self):
        return f"{self.first_name} {self.last_name}"