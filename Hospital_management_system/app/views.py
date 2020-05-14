from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from .models import *
# Create your views here.



def aboutus(request):
    return render(request,"aboutus.html")

def contactus(request):
    return render(request,"contactus.html")
def index(request):
    return render(request,"homepage.html")

def admin_login(request):
    error=""
    if request.method=='POST':
       un=request.POST['adm_un']
       psd=request.POST['adm_psd']
       user=authenticate(username=un,password=psd)
       try:
           if user.is_staff:
               login(request,user)
               error="no"
           else:
               error="yes"
       except:
           error="yes"
    return render(request,"admin_login.html",{"error":error})
def admin_home(request):
    return render(request,"admin_home.html")

def admin_logout(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    logout(request)
    return redirect('admin_login')

def add_doctor(request):
    error=''
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method=='POST':
        dn=request.POST['dt_name']
        dtcn=request.POST['dt_cntno']
        dtspl=request.POST['dt_spltn']
        try:
            Doctors.objects.create(d_name=dn,d_contactno=dtcn,d_specialization=dtspl)
            error='no'
        except:
            error="yes"
    return render(request,"add_doctor.html",{"error":error})

def view_doctor(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    dct=Doctors.objects.all()
    return render(request,"view_doctor.html",{"dct":dct})


def delete_doctor(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    rno=request.GET.get('rno')
    Doctors.objects.get(d_no=rno).delete()
    return redirect('view_doctor')


def add_patient(request):
    error=''
    if not request.user.is_staff:
        return redirect('admin_login')
    if request.method=='POST':
        pn=request.POST['pt_name']
        pg=request.POST['pt_gender']
        pcnt=request.POST['pt_cnt']
        pad=request.POST['pt_adr']
        try:
            Patient.objects.create(p_name=pn,gender=pg,p_contactno=pcnt,p_address=pad)
            error='no'
        except:
            error="yes"
    return render(request,"add_patient.html",{"error":error})

def view_patient(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    pt=Patient.objects.all()
    return render(request,"view_patient.html",{"pt":pt})

def delete_patient(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    rno=request.GET.get('rno')
    Patient.objects.get(p_no=rno).delete()
    return redirect('view_patient')

def add_appointment(request):
    error=''
    if not request.user.is_staff:
        return redirect('admin_login')
    doctor1=Doctors.objects.all()
    patient1=Patient.objects.all()
    if request.method=='POST':
        d=request.POST.get('doctor')
        p=request.POST.get('patient')
        print(d,p)
        doctor=Doctors.objects.filter(d_name=d).first()
        patient=Patient.objects.filter(p_name=p).first()
        print('1')
        try:
            Appointment.objects.create(doctor=doctor,paitent=patient)
            error='no'
        except:
            error='yes'

    return render(request,"add_appointment.html",{"error":error,"doctor":doctor1,"patient":patient1})

def view_appointment(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    at=Appointment.objects.all()
    return render(request,"view_appointment.html",{"at":at})

def delete_appointment(request):
    if not request.user.is_staff:
        return redirect('admin_login')
    rno=request.GET.get('rno')
    Appointment.objects.get(id=rno).delete()
    return redirect('view_appointment')
