from django.db import models

class Category(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField()

    def __str__(s):
        return s.title

class Image(models.Model):
    title=models.CharField(max_length=200)
    description=models.TextField()
    image=models.ImageField(upload_to='images')
    added_date=models.DateField()
    cat=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(s):
        return s.title
