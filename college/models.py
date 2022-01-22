from django.db import models


class university(models.Model):

    unid = models.AutoField
    unname = models.CharField(max_length=50)

    def __str__(self):
        return self.unname

class college(models.Model):

    cid = models.AutoField
    unid = models.ForeignKey(university, on_delete=models.CASCADE)
    cname = models.CharField(max_length=50)
    uname = models.CharField(max_length=50)
    cemail = models.CharField(max_length=50,default='')
    cmob = models.CharField(max_length=50)
    cadd = models.CharField(max_length=100)
    ccity = models.CharField(max_length=50)
    cweb = models.CharField(max_length=50)
    cdesc = models.CharField(max_length=500)
    cpass = models.CharField(max_length=20,default='12345')
    cimg = models.ImageField(upload_to="college/images", default='')


    def __str__(self):
        return self.cname

class course(models.Model):

    coid = models.AutoField
    cid = models.ForeignKey(college, on_delete=models.CASCADE, related_name="display")
    coname = models.CharField(max_length=50)

    def __str__(self):
        return self.coname

class branch(models.Model):

    brid = models.AutoField
    course = models.ForeignKey(course,on_delete=models.CASCADE,related_name="display")
    brname = models.CharField(max_length=50)

    def __str__(self):
        return self.brname

class subject(models.Model):

    suid = models.AutoField
    branch = models.ForeignKey(branch,on_delete=models.CASCADE,related_name="display")
    suname = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.suname


class Student(models.Model):
   
    sid=models.AutoField
    sname=models.CharField(max_length=50)
    colname = models.CharField(max_length=50)
    semail=models.CharField(max_length=50)
    smob=models.CharField(max_length=12)
    sadd=models.CharField(max_length=100)
    scity=models.CharField(max_length=50)
    scourse=models.CharField(max_length=50)
    sbranch=models.CharField(max_length=50)
    ssubject=models.CharField(max_length=20)
    sdesc=models.CharField(max_length=50)
    ssem=models.CharField(max_length=5)
    spass = models.CharField(max_length=20, default='12345')
    simg = models.ImageField(upload_to="college/images", default='')
    def __str__(self):
        return self.sname

class teacher(models.Model):

    tid = models.AutoField

    teacher_name = models.CharField(max_length=50)
    assignment_name =models.CharField(max_length=11)
    temail = models.CharField(max_length=50)
    tpass = models.CharField(max_length=50)
    file= models.FileField(upload_to="")

    def __str__(self):
        return self.teacher_name

class assignment(models.Model):
    aid =models.AutoField
    ass_name = models.CharField(max_length=10)
    ass_file = models.FileField(upload_to="")

    def __str__(self):
        return self.ass_name

