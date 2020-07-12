from django.shortcuts import render,redirect
from django.contrib import messages
from App.forms import CourseForm,StudentForm
from App.models import CourseModel,StudentModel,EnrollModel

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

#Admin Operation

def adminPage(request):
    return render(request,'admin_page.html')

def loginAdmin(request):
    un=request.POST.get('a1')
    pa=request.POST.get('a2')
    if un=='admin' and pa=='admin':
        return render(request,'login_admin.html')
    else:
        messages.error(request,'Invalid Username or Password')
        return redirect('admin_page')

def admin_home(request):
    return render(request,'login_admin.html')

def newCourse(request):
    return render(request,'new_course.html',{'data':CourseForm()})

def addCourse(request):

   pf=CourseForm(request.POST)
   if pf.is_valid():
       pf.save()
       messages.success(request,'Course saved successfully')
       return redirect('new_course')
   else:
       return render(request,'new_course.html',{'data':pf})

def view_all_course(request):
    return render(request,'view_all_course.html',{'data':CourseModel.objects.all()})

def update_course(request):
    no=request.GET.get('cid')
    return render(request,'update_course.html',{'data':CourseModel.objects.get(cid=no)})

def course_update(request):
    no=request.POST.get('u')
    na=request.POST.get('u1')
    fa=request.POST.get('u2')
    dt=request.POST.get('u3')
    tm=request.POST.get('u4')
    fe=request.POST.get('u5')
    dur=request.POST.get('u6')
    CourseModel.objects.filter(cid=no).update(name=na,faculty=fa,date=dt,time=tm,fee=fe,duration=dur)
    messages.success(request,'Course Updated Successfully')
    return redirect('view_all_course')

def delete_course(request):
    no=request.GET.get('cid')
    CourseModel.objects.get(cid=no).delete()
    messages.success(request,'Course deleted Successfully')
    return redirect('view_all_course')

#Student Operation
def student_page(request):
    return render(request,'student_login.html',{'data':CourseModel.objects.all()})

def register_student(request):
    return render(request,'register_student.html',{'data':StudentForm()})

def student_register(request):
    sf=StudentForm(request.POST)
    if sf.is_valid():
        sf.save()
        messages.success(request,'Student Register Successfully')
        return redirect('register_student')
    else:
        return render(request,'register_student.html',{'data':sf})

def login_student(request):
    return render(request,'login_student.html')

def student_login(request):
    un=request.POST.get('a1')
    pa=request.POST.get('a2')
    try:
        sm=StudentModel.objects.get(email=un,password=pa)
        return render(request,'student.html',{'data':sm})
    except StudentModel.DoesNotExist:
        messages.error(request,'Invalid User')
        return redirect('login_student')


def student_home(request):
    return render(request, 'student.html')

def enroll_course(request):
    return render(request,'enroll_course.html',{'data':CourseModel.objects.all(),'sdata':StudentModel.objects.all()})


def contact_us(request):
    return render(request,'contact_us.html')