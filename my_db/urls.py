"""my_db URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from my_app import views
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.base, name ='index'),
    path('login/',views.login,name = 'login'),
    path('signup/',views.signup, name= 'signup'),
    path('instructor/',views.instructor, name= 'instructor'),
    path('inst_signup/',views.instsignup, name= 'inst_signup'),
    path('inst_login/',views.instlogin, name= 'inst_login'),
    path('user_page/',views.userpage, name= 'userpage'),
    path('mycourse/<int:pk>/',views.mycourse, name= 'mycourse'),
    path('inst_page/',views.instpage, name= 'instpage'),
    path('signout/',views.signout, name='signout'),
    path('addcourse/',views.addcourse, name='addcourse'),
    path('corusel/',views.corusel, name='corusel'),
    path('navbar/',views.navbar, name='navbar'),
    path('pdfs/',views.pdfs, name='pdfs'),
    path('videos/',views.videos, name='videos'),
    path('quiz/',views.quiz, name='quiz'),
    path('main/<int:pk>/<int:usr>/', views.main_view, name="main-view"),
    path('rate/', views.rate_image, name='rate-view'),
    path('coursedetail/<int:pk>/<int:user>/',views.coursedetail,name='coursedetail'),
    path('courseview/<int:pk>/<int:user>/', views.courseview, name='courseview'),
    path('search/',views.search,name='search'),
    path('instructor_page/',views.instructorpage,name='instructorpage'),
    path('instructor2/',views.instructor2,name='instructor2'),
   
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
