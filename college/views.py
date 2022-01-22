from django.shortcuts import render ,redirect
from college.models import college, university, course,  Student, branch, teacher
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth import logout as logouts



# Create your views here.
def index(request):
    # print('you are:', request.session.get('lid'))
    return render(request,'college/index.html')


def about(request):
    
    return render(request,'college/about.html')

def contact(request):
    return render(request,'college/contact.html')

def collegereg(request):
      if request.method == 'POST':
        cnm = request.POST['cnm']
        u = request.POST['unm']
        ceid = request.POST['ceid']
        cmno = request.POST['cmno']
        cadd = request.POST['cadd']
        ccity = request.POST['ccity']
        cweb = request.POST['cweb']
        cdesc = request.POST['cdesc']
        
        univ = university.objects.get(id=u)

        #print(cnm)
        r = college(cname=cnm, uname=u,cemail=ceid, cmob=cmno, cadd=cadd, ccity=ccity, cweb=cweb, cdesc=cdesc,unid =univ)
        r.save()
        params = {'data': 'data submitted'}
        return render(request, 'college/collegesubmit.html', params)
      else:
          unm = university.objects.all()
          dict = {'university':unm}
          return render(request, 'college/collegereg.html',dict)

def studentreg(request):
    if request.method == 'POST':
        scol =request.POST['scol']
        scour =request.POST['scor']
        sbr=request.POST['sbr']
        ssub=request.POST['ssub']
        sname = request.POST['snm']
        seid = request.POST['seid']
        smno = request.POST['smno']
        sadd = request.POST['sadd']
        scity = request.POST['scity']
        sdesc = request.POST['sdesc']
        simg = request.FILES['simg']

    
        z = Student(simg=simg,ssubject=ssub,sbranch=sbr,scourse=scour,colname=scol,sname=sname, semail=seid, smob=smno, sadd=sadd, scity=scity, sdesc=sdesc)
        z.save()
        
      
        return HttpResponse('your record submit')
        
    return render(request, 'college/studentreg.html')


def collegesubmit(request):
    return render(request,'college/collegesubmit.html')


def collegeprofile(request):
    cc=request.GET.get('c')
    path = college.objects.get(cname=cc)
    dict = {'cpdata': path}
    return HttpResponse(render(request, 'college/collegeprofile.html', dict))

def edit(request,id=None):
    if request.method == 'POST':
        cid = request.POST['id']
        fn = request.POST['fullname']
        ce = request.POST['email']
        cc = request.POST['city']
        cw = request.POST['web']
        cd = request.POST['desc']
        cm = request.POST['mobile']


        college.objects.filter(id=cid).update(cname=fn,cemail=ce,ccity=cc,cweb=cw,cdesc=cd,cmob=cm)
        user = college.objects.get(id=cid)
        params = {'data': 'data updated','user':user}
        return render(request, 'college/edit.html', params)

    else:

        user = course.objects.get
        param={'user':user}

    return render(request, 'college/edit.html',param)

def courseedit(request):
    if request.method == 'POST':
        cid = request.POST['id']
        fn = request.POST['fullname']
        coid = request.POST['courseid']

        course.objects.filter(id=coid).update(coname=fn)
        user = college.objects.get(id=cid)
        c = course.objects.get(id=coid)
        
        courses = course.objects.filter(cid=cid)
        params = {'data': 'data updated', 'user': user, 'course': c, 'courses': courses}
        return render(request, 'college/courseedit.html', params)

    else:
       
        
        user = course.objects.get
        param = {'user': user}
        
    return render(request,'college/courseedit.html',param)

def delete(request):

    user = college.objects.get.delete()
    param = {'user': user}
    return render(request, 'college/delete.html', param)

def teacherlogin(request):
    if request.method == 'POST':

        tem = request.POST['t-mail']
        tpa = request.POST['t-pass']
        t = teacher.objects.get(temail=tem, tpass=tpa)
        request.session['lid'] = tem
        messages.success(request, "successfully logged in")
        params = {'data': t}

        return render(request, 'college/teacherindex.html', params)
    else:
        messages.error(request, "Invalid credentials,Please try again")
    return render(request,'college/teacherlogin.html')

def teacherlogout(request):
    if request.method=='POST':
        logouts(request)
        return redirect(college/index)
    

def teacherindex(request):
    if request.method == 'POST':
        f_name = request.POST.get('filename')
        ass = request.POST.get('ass')
        myfile = request.FILES.getlist('uploadfiles')
        for f in myfile:
            teacher(teacher_name=f_name,file=f,assignment_name=ass).save()

        # print(myfile)
        return HttpResponse('ok')
    
    
    return render(request, 'college/teacherindex.html')

def download(request):
    Teacher=request.GET.get('teacher')
    Teacher = teacher.objects.all()
    # print(Teacher)
    params ={'teacher':Teacher}
    return render(request,'college/download.html',params)


