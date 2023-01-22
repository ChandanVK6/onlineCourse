from django.shortcuts import render,redirect
from .models import Courses
from .models import User
from django.http import HttpResponse ,HttpRequest
# Create your views here.
from django.contrib import messages
from django.views import View
from .models import (Instructor,Category,Pdfs,Videos,Quiz,Rating,Courses,Courses_User)

usr_sign_fname =''
usr_sign_lname=''
usr_sign_sex=''
usr_sign_email=''
usr_sign_passw=''
usr_login_passw=''
usr_login_email=''
user=''

ins_sign_fname =''
ins_sign_lname=''
ins_sign_sex=''
ins_sign_email=''
ins_sign_passw=''
ins_login_passw=''
ins_login_email=''

def base(request):
    return render(request,'base.html')

def login(request):
    global usr_login_email,usr_login_passw
    courses = Courses.objects.all()
    if request.method=="POST":
        
        usr_login_email = request.POST['Email']
        usr_login_passw = request.POST['password']
        for usr in User.objects.all():
            if usr_login_email ==usr.email and usr_login_passw ==usr.passwd:
                programming = Courses.objects.filter(category_id = '2')
                web_development = Courses.objects.filter(category_id ='3')
                mobile_development = Courses.objects.filter(category_id ='4')
                data_science = Courses.objects.filter(category_id = '1')
                return render(request,'user_page.html',{'usr':usr,'courses':courses,'programming': programming ,'web_development': web_development, 'mobile_development': mobile_development,'data_science':data_science})


    return render(request,'login.html')



def signup(request):
    global usr_sign_email,usr_sign_fname,usr_sign_lname,usr_sign_passw,usr_sign_sex
    if request.method=="POST":
        usr_sign_fname = request.POST['firstname']
        usr_sign_lname = request.POST['lastname']
        usr_sign_email = request.POST['Email']
        usr_sign_passw = request.POST['password']
        usr_sign_sex = request.POST['sex']

        u = User(fname=usr_sign_fname,lname=usr_sign_lname,email=usr_sign_email,passwd=usr_sign_passw,sex=usr_sign_sex)
        for usr in User.objects.all():
            if usr_sign_fname == usr.fname and usr_sign_lname == usr.lname:
                return render(request,'signup.html')
        u.save()
        return redirect('login')
    return render(request,'signup.html')




def instructor(request):
    return render(request,'instructor.html')




def instsignup(request):
    global ins_sign_email,ins_sign_fname,ins_sign_lname,ins_sign_passw,ins_sign_sex
    if request.method=="POST":
        ins_sign_fname = request.POST['firstname']
        ins_sign_lname = request.POST['lastname']
        ins_sign_email = request.POST['Email']
        ins_sign_passw = request.POST['password']
        ins_sign_sex = request.POST['sex']

        u = Instructor(fname=ins_sign_fname,lname=ins_sign_lname,email=ins_sign_email,passwd=ins_sign_passw,sex=ins_sign_sex)
        for ins in Instructor.objects.all():
            if ins_sign_fname == ins.fname and ins_sign_lname == ins.lname:
                return render(request,'inst_signup.html')
        u.save()
        
        for ins in Instructor.objects.all():
            if ins_sign_fname == ins.fname and ins_sign_lname == ins.lname:
                return render(request,'instlogin.html')
    return render(request,'inst_signup.html')



def instlogin(request):
    global ins_login_email,ins_login_passw
    if request.method=="POST":
        ins_login_email = request.POST['Email']
        ins_login_passw = request.POST['password']
        for inst in Instructor.objects.all():
            if ins_login_email ==inst.email and ins_login_passw ==inst.passwd:
                return render(request,'inst_page.html',{'ins':inst})
    return render(request ,'inst_login.html')
     


def userpage(request):
    programming = Courses.objects.filter(category_id = '2')
    web_development = Courses.objects.filter(category_id ='3')
    mobile_development = Courses.objects.filter(category_id ='4')
    data_science = Courses.objects.filter(category_id = '1')
    return render(request, 'user_page.html',{'programming': programming ,'web_development': web_development, 'mobile_development': mobile_development,'data_science':data_science})

    

def mycourse(request,pk):
    usrs = User.objects.get(pk=pk)
    users = Courses_User.objects.filter(user_id=pk)
    return render(request,'mycourse.html',{'user':users,'usrs':usrs})
    

def instpage(request):
    return render(request,'inst_page.html')


def signout(request):
    global usr_sign_email,usr_sign_fname,usr_sign_lname,usr_sign_passw,usr_sign_sex,usr_login_email,usr_login_passw,ins_sign_email,ins_sign_fname,ins_sign_lname,ins_sign_passw,ins_sign_sex,ins_login_email,ins_login_passw,user
    usr_sign_fname = ''
    usr_sign_lname = ''
    usr_sign_email = ''
    usr_sign_passw = ''
    usr_sign_sex = ''
    usr_login_email = ''
    usr_login_passw = ''
    user=''
    ins_sign_fname =''
    ins_sign_lname=''
    ins_sign_sex=''
    ins_sign_email=''
    ins_sign_passw=''
    ins_login_passw=''
    ins_login_email=''
    return render(request,'signout.html')

def addcourse(request):
    global ins_login_email,ins_login_passw
    Cat = Category.objects.all()
    cat = Courses.objects.all()
    for ins in Instructor.objects.all():
            if ins_login_email == ins.email and ins_login_passw == ins.passwd:
                if request.method=="POST":
                    cour_name = request.POST['name']
                    cour_content = request.POST['content']
                    cour_cat = request.POST.get('category')
                    cour_ins = request.POST.get('instructor')
                    cour_img = request.FILES.get('image')
                    cour_intro = request.POST['intro']
                    category = Category.objects.get(name=cour_cat)
                    u = Courses.objects.create(name=cour_name,content=cour_content,category_id_id=category.pk,instructor_id=ins.pk,image=cour_img,intro_Video=cour_intro)
                    m= Rating.objects.create(courses_id_id=u.pk)
                    m.save()
                    u.save()
                    return redirect('pdfs')
                else:
                    return render(request,'addcourse.html',{
                        'ins':ins,
                        'category':Cat
                        }) 
                
    return render(request,'addcourse.html')



def corusel(request):
    return render(request,'corousel.html')



def navbar(request):
    return render(request,'navbar.html')

def pdfs(request):
    global ins_login_email,ins_login_passw
    cat = Courses.objects.all()
    for ins in Instructor.objects.all():
            if ins_login_email == ins.email and ins_login_passw == ins.passwd:
                if request.method =="POST":
                    pdf_name = request.POST['name']
                    pdf_pdf = request.FILES.get('pdf')
                    pdf_cour = request.POST.get('courses')
                    course = Courses.objects.get(name=pdf_cour)
                    u = Pdfs.objects.create(pdf_name=pdf_name,file=pdf_pdf,course_id=course.pk)
                    u.save()
                    return redirect('videos')
                else:
                    return render(request,'pdf.html',{'Courses':cat,'ins':ins}) 
    return render(request,'pdf.html')


def videos(request):
    global ins_login_email,ins_login_passw
    cat = Courses.objects.all()
    for ins in Instructor.objects.all():
            if ins_login_email == ins.email and ins_login_passw == ins.passwd:
                if request.method=="POST":
                    vid_name = request.POST['name']
                    vid_video = request.POST['video']
                    vid_cour = request.POST.get('courses')
                    course = Courses.objects.get(name=vid_cour)
                    u = Videos.objects.create(vid_name=vid_name,vid=vid_video,course_id=course.pk)
                    u.save()
                    return redirect('quiz')
                else:
                    return render(request,'video.html',{'Courses':cat,'ins':ins}) 
    return render(request,'video.html')

def quiz(request):
    global ins_login_email,ins_login_passw
    cat = Courses.objects.all()
    for ins in Instructor.objects.all():
            if ins_login_email == ins.email and ins_login_passw == ins.passwd:
                if request.method=="POST":
                    qui_name = request.POST['name']
                    qui_url = request.POST['quiz']
                    qui_cour = request.POST.get('courses')
                    course = Courses.objects.get(name=qui_cour)
                    u = Quiz.objects.create(quiz_name=qui_name,quiz_url=qui_url,course_id=course.pk)
                    u.save()
                    return render(request,'inst_page.html',{'ins':ins})
                else:
                    return render(request,'quiz.html',{'Courses':cat,'ins':ins}) 
    return render(request,'quiz.html')





from .models import Rating
from django.http import JsonResponse


def main_view(request,pk,usr):
    usr = User.objects.get(pk=usr)
    courses = Courses.objects.get(pk=pk)
    courses.user.add(usr, through_defaults={'enroll_date':1})
    obj = Rating.objects.get(courses_id =pk)  
    context ={
        'object': obj,
        'courses':courses,
        'usr':usr
    }
    return render(request, 'index.html', context)


def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'})




def courseview(request,pk,user):
    user = User.objects.get(pk=user)
    courses = Courses.objects.get(pk=pk)
    return render(request,'courseview.html',{'courses':courses,'usr':user})



def coursedetail(request,pk,user):
    user = User.objects.get(pk=user)
    score =[]
    courses = Courses.objects.get(pk=pk)
    videos = Videos.objects.filter(course=courses.pk)
    pdf = Pdfs.objects.filter(course=courses.pk)
    quiz = Quiz.objects.filter(course=courses.pk)
    rate = Rating.objects.filter(courses_id=courses.pk)
    for no in rate:
        score.append(no.score)
    avr = sum(score)/len(score)
    average = round(avr,3)
    if average == 1:
        return render(request,'courseDetail.html',{'courses':courses,'videos':videos,'pdf':pdf,'quiz':quiz,'one':average,'usr':user})
    elif average == 2:
        return render(request,'courseDetail.html',{'courses':courses,'videos':videos,'pdf':pdf,'quiz':quiz,'two':average,'usr':user})
    elif average == 3:
        return render(request,'courseDetail.html',{'courses':courses,'videos':videos,'pdf':pdf,'quiz':quiz,'three':average,'usr':user})
    elif average == 4:
        return render(request,'courseDetail.html',{'courses':courses,'videos':videos,'pdf':pdf,'quiz':quiz,'four':average,'usr':user})
    elif average == 5:
        return render(request,'courseDetail.html',{'courses':courses,'videos':videos,'pdf':pdf,'quiz':quiz,'five':average,'usr':user})
