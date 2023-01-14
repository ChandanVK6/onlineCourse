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
    path('',views.index, name ='index'),
    path('login/',views.login,name = 'login'),
    path('signup/',views.signup, name= 'signup'),
    path('instructor/',views.instructor, name= 'instructor'),
    path('inst_signup/',views.instsignup, name= 'inst_signup'),
    path('inst_login/',views.instlogin, name= 'inst_login'),
    path('user_page/<int:name>/',views.userpage, name= 'userpage'),
    path('mycourse/',views.mycourse, name= 'mycourse'),
]+ static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
