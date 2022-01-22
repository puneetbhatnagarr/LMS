from ast import Param
from urllib import request
from django.shortcuts import render , HttpResponse , redirect
from django.contrib import messages
from college.models import college, Student , assignment
from django.contrib.auth import logout as logouts


# Create your views here.
def index(request):
    print('you are:', request.session.get('lid'))
    return render(request,'index.html')

def studentindex(request):
    print('you are:', request.session.get('lid'))
    
    if request.method == 'POST':
        file_name = request.POST.get('filename')
        myfile = request.FILES.getlist('uploadfiles')
        for sf in myfile:
            assignment(ass_name=file_name , ass_file=sf).save()
        # print(sfile)
        return HttpResponse('ok')
    
    return render(request,'studentindex.html')


def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def showcollege(request):
    obj = college.objects.all()
    params = {'data': obj}
    return render(request,'showcollege.html',params)

def login(request):
    # if request.session.has_key('loginid'):
    if request.method == 'POST':

        e = request.POST['email']
        p = request.POST['pass']
        c = college.objects.get(cemail=e, cpass=p)
        request.session['lid'] = e
        messages.success(request, "successfully logged in")
        params = {'data': c}

        return render(request, 'college/index.html', params)
    else:
        messages.error(request, "Invalid credentials,Please try again")

    return render(request,'login.html')

def logout(request):
    if request.method=='POST':
        logouts(request)
        
    return render(request,'index.html')

def studentlogin(request):
    if request.method == 'POST':

        em = request.POST['e-mail']
        pa = request.POST['s-pass']
        s = Student.objects.get(semail=em, spass=pa)
        request.session['lid'] = em
        messages.success(request, "successfully logged in")
        params = {'data': s}

        return render(request, 'studentindex.html', params)
    else:
        messages.error(request, "Invalid credentials,Please try again")
    return render(request,'studentlogin.html')



def search(request):
   s=request.GET['se']
   data=college.objects.filter(cname__icontains=s)
   print(data)
   params={'data':data}
   return render(request,'search.html',params)

def studentsearch(request):
   ss=request.GET['ssearch']
   obj=Student.objects.filter(sname__icontains=ss)
   print(obj)
   params={'obj':obj}
   return render(request,'studentsearch.html',params)

def studentprofile(request):
    student = request.GET.get('Student')
    student = Student.objects.all()
    Params = {'Student':student} 
    return render(request,'studentprofile.html',Params)
