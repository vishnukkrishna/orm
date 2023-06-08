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


class Product(models.Model):
    name=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    quantity=models.PositiveIntegerField()



    def __str__(self):
        return self.name




class Subjects(models.Model):
    subject = models.CharField(max_length=50)

    def __str__(self) :
        return self.subject




class Teachers(models.Model):
    name = models.CharField(max_length=50)
    subject = models.ForeignKey(Subjects,on_delete=models.SET_NULL,null=True)
    
    def __str__(self) :
            return str(self.name)
    



class Class(models.Model):
    class_name = models.CharField(max_length=50)
    class_teacher = models.ForeignKey(Teachers,on_delete=models.SET_NULL,null=True)
    strength = models.IntegerField(default=0)

  
    def __str__(self) :
        return self.class_name
    



class Student(models.Model):

    GENDER_CHOICE = [
        ('male','Male'),
        ('female','Female'),
    ]

    name = models.CharField(max_length=50)
    class_name = models.ForeignKey(Class,on_delete=models.SET_NULL,null=True)
    dob = models.DateField(null=True,blank=True)
    roll_no = models.IntegerField(unique=True)
    gender = models.CharField(max_length=10,choices=GENDER_CHOICE,default='Not defined')

    def __str__(self):
        return self.name