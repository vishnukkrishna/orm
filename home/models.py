from django.db import models

# Create your models here.

class Book(models.Model):

    name=models.CharField(max_length=200)

    description=models.TextField(blank=True)

    pages=models.IntegerField()

    price=models.DecimalField( max_digits=10, decimal_places=2)

    auther=models.CharField(max_length=100,null=True)


    def __str__(self):

        return self.name
    

    class Meta:

        verbose_name_plural='books'
    


class Users(models.Model):

    username=models.CharField(max_length=20)

    Book=models.ForeignKey(Book,on_delete=models.CASCADE)



    def __str__(self):

        return self.username
    

    class Meta:

        verbose_name_plural='users'