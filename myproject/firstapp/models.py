from django.db import models


class Allcourses(models.Model):
    objects = None
    coursename = models.CharField(max_length=200)
    instruct = models.CharField(max_length=200)

    def __str__(self):
        return self.coursename


class Details(models.Model):
    course = models.ForeignKey(Allcourses, on_delete=models.CASCADE)
    sp = models.CharField(max_length=500)
    il = models.CharField(max_length=500)

    def __str__(self):
        return self.sp
