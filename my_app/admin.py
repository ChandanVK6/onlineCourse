from django.contrib import admin

# Register your models here.
from .models import (User,Instructor,Category,Courses,Videos,Quiz,Pdfs,rating)

admin.site.register(User)
admin.site.register(Instructor)
admin.site.register(Category)
admin.site.register(Courses)
admin.site.register(Videos)
admin.site.register(Quiz)
admin.site.register(Pdfs)
admin.site.register(rating)