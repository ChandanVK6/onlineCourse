from django.db import models

# Create your models here.

class User(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20,null=True)
    email = models.EmailField(max_length =50,null=True)
    passwd = models.CharField(max_length = 16,null=True)
    sex = models.CharField(max_length =10)

    def __str__(self):
        return self.fname  
        

class Instructor(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20,null=True)
    skills = models.TextField(max_length = 40)
    email = models.EmailField(max_length =50,null=True)
    passwd = models.CharField(max_length = 16,null=True)
    sex = models.CharField(max_length =10)


    def __str__(self):
        return str(self.fname + self.lname)

class Category(models.Model):
    name = models.CharField(max_length = 20)
    description = models.TextField(max_length = 50)
    instructor = models.ForeignKey(Instructor,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.name


class Courses(models.Model):
    name = models.CharField(max_length = 20)
    content = models.TextField(max_length = 50)
    category = models.ForeignKey(Category,on_delete = models.CASCADE,null = True)
    instructor = models.ForeignKey(Instructor,on_delete = models.CASCADE,null = True)
    user = models.ManyToManyField(User)
    image = models.ImageField(null = True,blank = True,upload_to = 'images/')

    def __str__(self):
        return self.name

class Videos(models.Model):
    file = models.URLField()
    course = models.ForeignKey(Courses,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return self.file 


class Quiz(models.Model):
    quiz_url = models.URLField(null=True)
    course = models.ForeignKey(Courses,on_delete = models.CASCADE,null=True)


    def __str__(self):
        return self.quiz_url


class Pdfs(models.Model):
   
    pdf_file  = models.FileField(upload_to ='pdfs/',null = True,verbose_name = '')
    course = models.ForeignKey(Courses,on_delete = models.CASCADE,null=True)

    def __str__(self):
        return str(self.pdf_file)


class rating(models.Model):
   
    rev_stars = models.IntegerField()
    course = models.ForeignKey(Courses,on_delete=models.CASCADE,null=True)


    def __str__(self):
        return str(self.rev_stars)

