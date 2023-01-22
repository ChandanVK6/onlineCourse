from  embed_video.fields  import  EmbedVideoField
# Create your models here.
from django.db import models
from django.db.models import Avg
from django.core.validators import MaxValueValidator, MinValueValidator

class User(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField(max_length =50)
    passwd = models.CharField(max_length = 16)
    sex = models.CharField(max_length =10)

    def __str__(self):
        return self.fname +' '+ self.lname

class Instructor(models.Model):
    fname = models.CharField(max_length = 20)
    lname = models.CharField(max_length = 20)
    email = models.EmailField(max_length =50)
    passwd = models.CharField(max_length = 16)
    sex = models.CharField(max_length =10)
    image = models.ImageField(null = True,blank = True,upload_to = 'images/')

    def __str__(self):
        return self.fname +' '+ self.lname

class Category(models.Model):
    category_id = models.BigAutoField(primary_key =True)
    name = models.CharField(max_length = 50)
   

    def __str__(self):
        return self.name
  



class Courses(models.Model):
    courses_id = models.BigAutoField(primary_key = True)
    name = models.CharField(max_length = 50)
    content = models.TextField(max_length = 50)
    category_id = models.ForeignKey(Category,on_delete = models.CASCADE)
    instructor = models.ForeignKey(Instructor,on_delete = models.CASCADE)
    user = models.ManyToManyField(User,related_name ="user",through="Courses_User")
    image = models.ImageField(upload_to = 'images/')
    intro_Video = EmbedVideoField()

   
    def __str__(self):
        return self.name

class Videos(models.Model):
    vid_name = models.CharField(max_length=50)
    vid = EmbedVideoField()
    course = models.ForeignKey(Courses,on_delete = models.CASCADE)
    
    def __str__(self):
        return self.vid_name
   

class Quiz(models.Model):
    quiz_name = models.CharField(max_length=50)
    quiz_url = models.URLField()
    course= models.ForeignKey(Courses,on_delete = models.CASCADE)
    

    def __str__(self):
        return self.quiz_name
   


class Pdfs(models.Model):
    pdf_name = models.CharField(max_length=50)
    file  = models.FileField(upload_to ='pdfs/')
    course = models.ForeignKey(Courses,on_delete = models.CASCADE)
   

    def __str__(self):
        return self.pdf_name


class Rating(models.Model):
    courses_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    score = models.IntegerField(default=0,
        validators=[
            MaxValueValidator(5),
            MinValueValidator(0),
        ]
    )

    def __str__(self):
        return str(self.pk)



class Courses_User(models.Model):
    courses_id = models.ForeignKey(Courses,on_delete=models.CASCADE)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
    enroll_date =  models.DateTimeField(auto_now_add=True) 

    class Meta:
        unique_together = ("user_id","courses_id")
