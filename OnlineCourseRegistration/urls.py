"""OnlineCourseRegistration URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

from App import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.showIndex,name='main'),
    path('admin_page/',views.adminPage,name='admin_page'),
    path('login_admin/',views.loginAdmin,name='login_admin'),
    path('admin_home/',views.admin_home,name='admin_home'),
    path('new_course/',views.newCourse,name='new_course'),
    path('add_course/',views.addCourse,name='add_course'),
    path('view_all_course/',views.view_all_course,name='view_all_course'),
    path('update_course/',views.update_course,name='update_course'),
    path('course_update/',views.course_update,name='course_update'),
    path('delete_course/',views.delete_course,name='delete_course'),

    #Student Operation
    path('student_page/',views.student_page,name='student_page'),
    path('register_student/',views.register_student,name='register_student'),
    path('student_register/',views.student_register,name='student_register'),
    path('login_student/',views.login_student,name='login_student'),
    path('student_login/',views.student_login,name='student_login'),
    path('student_home/',views.student_home,name='student_home'),
    path('enroll_course/',views.enroll_course,name='enroll_course'),
    path('contact_us/',views.contact_us,name='contact_us')

]
