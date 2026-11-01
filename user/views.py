from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):    
    cat=tbl_category.objects.all()[:12]
    job=tbl_job.objects.select_related('company').all().order_by("-id")[:8]
    comp=tbl_company.objects.all()[:20]
    city=tbl_city.objects.all()[:20]
    mydict={"cat":cat,"job":job,"comp":comp,"city":city}
    return render(request,"user/index.html",mydict)

def contact(request):
    mydict={}
    if request.method=="POST":
        a=request.POST.get("name")
        b=request.POST.get("mobile")
        c=request.POST.get("email")
        d=request.POST.get("message")
        tblcontact(name=a,mobile=b,email=c,message=d).save()
        mydict={"msg":"Thank you for contact with us"}        
    return render(request,"user/contact.html",mydict)

def about(request):
    return render(request,"user/about.html")

def gallery(request):
    data=tblgallery.objects.all()
    mydict={'gdata':data}
    return render(request,"user/gallery.html",mydict)

def team(request):
    data=tblteam.objects.all()
    mydict={'tdata':data}
    return render(request,"user/team.html",mydict)

def profile(request):
    return render(request,"user/profile.html")

def uprofile(request):
    return render(request,"uprofile.html")

def registration(request):
    if request.method=="POST":
        Name=request.POST.get("name")
        Email=request.POST.get("email")
        Mobile=request.POST.get("mobile")
        Password=request.POST.get("password")
        Address=request.POST.get("address")
        ppic=request.FILES["fu"]
        gender=request.POST.get("gender")
        dob=request.POST.get("dob")
        skills=request.POST.get("skills")
        education=request.POST.get("education")
        experience=request.POST.get("experience")
        resume=request.FILES["resume"]
        x=tbl_register.objects.all().filter(email=Email).count()
        if x==0:
            tbl_register(name=Name,mobile=Mobile,email=Email,password=Password,address=Address,profile_picture=ppic,gender=gender,dob=dob,education=education,skills=skills,experience=experience,resume=resume).save()
            return HttpResponse("<script>alert('You Are Registered Successfully..');location.href='/user/registration/'</script>")
        else:
            return HttpResponse("<script>alert('You Are Already Registered.');location.href='/user/registration/'</script>")
            
    return render(request,"user/register.html")

def login(request):
    if request.method=="POST":
        Email=request.POST.get("email")
        Password=request.POST.get("password")
        x=tbl_register.objects.all().filter(email=Email,password=Password).first()
        if x:
            request.session["email"]=x.email
            request.session["uname"]=str(x.name)
            request.session["upic"]=str(x.profile_picture)
            return HttpResponse("<script>location.href='/user/jobs/'</script>")
        else:
            return render(request,"user/login.html",{"msg":"Your Email id or Password is Incorrect"})
    return render(request,"user/login.html")


def dashboard(request):
    return render(request,"dashboard.html")


def company(request):
    comp=tbl_company.objects.select_related('city').all()
    data={"comp":comp}
    return render(request,"user/company.html",data)


def jobs(request):
    job=tbl_job.objects.select_related('company').all().order_by("-id")
    cid=request.GET.get('cid')
    if cid:
        job=tbl_job.objects.select_related('company').filter(category=cid).order_by("-id")
    cityid=request.GET.get('cityid')
    if cityid:
        job=tbl_job.objects.select_related('company').filter(city=cityid).order_by("-id")
    compid=request.GET.get('compid')
    if compid:
        job=tbl_job.objects.select_related('company').filter(company=compid).order_by("-id")
    if request.method=="POST":
            title=request.POST.get("title")
            city=request.POST.get("city")
            exp=request.POST.get("exp")
            job=tbl_job.objects.select_related('company').filter(Q(title__icontains=title),Q(experience__icontains=exp),Q(city__name__icontains=city)).order_by("-id")
    data={"job":job}
    return render(request,"user/jobs.html",data)


def jobdetail(request):
    data={}
    jid=request.GET.get('jid')
    if jid:
        job=tbl_job.objects.select_related('company').filter(id=jid).order_by("-id")
        data={"job":job}
    return render(request,"user/jobdetail.html",data)

def apply(request):
    userid=request.session.get('email')
    jid=request.GET.get('jid')
    if userid is None:
        return HttpResponse("<script>alert('Login First to Apply.');location.href='/user/login/'</script>")
    else:
        user=tbl_register.objects.get(email=userid)
        job=tbl_job.objects.get(id=jid)
        x=tbl_apply.objects.all().filter(user=userid,job=jid).count()
        if x==0:
            tbl_apply(user=user,job=job).save()
            return HttpResponse("<script>alert('Successfully Applied.Please wait for Admin response.');location.href='/user/myjobs/'</script>")
        else:
            return HttpResponse("<script>alert('Already applied on this job. Kindly check My Job for update.');location.href='/user/myjobs/'</script>")
    return render(request,"user/dsdgsgd.html")

def myjobs(request):
    userid=request.session.get('email')
    job=tbl_apply.objects.select_related('job').filter(user=userid).order_by('-id')
    a=tbl_apply.objects.filter(user=userid).count() #total
    u=tbl_apply.objects.filter(user=userid,status='Under Review').count() #review
    s=tbl_apply.objects.filter(user=userid,status='Selected').count() #selected
    r=tbl_apply.objects.filter(user=userid,status='Rejected').count() #rejected
    l=tbl_apply.objects.filter(user=userid,status='Shortlisted').count() #shorted
    ap=tbl_apply.objects.filter(user=userid,status='Applied').count() #applied
    mydict={"job":job,'a':a,'u':u,'s':s,'r':r,'l':l,'ap':ap}
    return render(request,"user/myjobs.html",mydict)

def delete(request):
    userid=request.session.get('email')
    jid=request.GET.get('jid')
    tbl_apply.objects.filter(user=userid,job=jid).delete()
    return HttpResponse("<script>alert('Applied job deleted successfully.');location.href='/user/myjobs/'</script>")
def home(request):
    return HttpResponse("My Home Page")



