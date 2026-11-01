from django.shortcuts import render,redirect
from user.models import *
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request,"jobseeker/index.html")

def profile(request):
    user=request.session.get("email")
    data=""
    if user:
        data=tbl_register.objects.all().filter(email=user)
        if request.method=="POST":
            name=request.POST.get("name")
            mobile=request.POST.get("mobile")
            password=request.POST.get("password")
            address=request.POST.get("address")
            picture=request.FILES["fu"]
            tbl_register(name=name,mobile=mobile,password=password,address=address,profile_picture=picture,email=user).save()
            return HttpResponse("<script>alert('Your Profile is Updated Successfully..');location.href='/jobseeker/profile/'</script>")
    return render(request,"jobseeker/profile.html",{"userinfo":data})

def logout(request):
    user=request.session.get("email")
    if user:
        del request.session["email"]
        del request.session["uname"]
        del request.session["upic"]
        return redirect("/user/login/")
    return render(request,"user/logout.html")