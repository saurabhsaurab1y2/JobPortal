from django.db import models
from tinymce.models import HTMLField
from django.utils import timezone

# Create your models here.
#tblcontact

class tblcontact(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    email=models.CharField(max_length=50,null=True)
    message=models.TextField(null=True)


class tblgallery(models.Model):
    title=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="static/picture/",null=True)


class tblteam(models.Model):
    name=models.CharField(max_length=200,null=True)
    designation=models.CharField(max_length=200,null=True)
    picture=models.ImageField(upload_to="static/team/",null=True)            


class tbl_register(models.Model):
    name=models.CharField(max_length=50,null=True)
    mobile=models.CharField(max_length=15,null=True)
    email=models.EmailField(primary_key=True)
    password=models.CharField(max_length=30,null=True)
    address=models.TextField(null=True)
    profile_picture=models.ImageField(upload_to="static/profile/",null=True)
    gender=models.CharField(max_length=50,null=True)
    dob=models.DateField(null=True)
    skills=models.CharField(max_length=250,null=True)
    education=models.CharField(max_length=200,null=True)
    experience=models.CharField(max_length=100,null=True)
    resume=models.ImageField(upload_to="static/resume/",null=True)
    def __str__(self):
        return self.email

class tbl_category(models.Model):
    name=models.CharField(max_length=50,null=True)
    icon=models.ImageField(upload_to="static/caticon/",null=True)
    def __str__(self):
        return self.name    

class tbl_city(models.Model):
    name=models.CharField(max_length=50,null=True)
    icon=models.ImageField(upload_to="static/cityicon/",null=True)
    state=models.CharField(max_length=100,null=True)
    country=models.CharField(max_length=100,null=True)
    def __str__(self):
        return self.name   
     

class tbl_company(models.Model):
    name=models.CharField(max_length=50,null=True)
    logo=models.ImageField(upload_to="static/logo/",null=True)
    email=models.EmailField(max_length=200,null=True)
    mobile=models.IntegerField(null=True)
    address=models.TextField(null=True)
    owner=models.CharField(max_length=50,null=True)
    hr=models.CharField(max_length=50,null=True)
    hrcontact=models.IntegerField(null=True)
    city=models.ForeignKey(tbl_city,on_delete=models.CASCADE)
    def __str__(self):
        return self.name


class tbl_job(models.Model):
    title=models.CharField(max_length=250,null=True)
    company=models.ForeignKey(tbl_company,on_delete=models.CASCADE)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
    city=models.ForeignKey(tbl_city,on_delete=models.CASCADE)
    detail=HTMLField()
    salary=models.IntegerField(null=True)
    experience=models.CharField(max_length=100,null=True)
    vacancy=models.IntegerField(null=True)
    lastdate=models.DateField(null=True)
    jobtype=models.CharField(max_length=100,null=True)
    posted_on=models.DateField(null=True,default=timezone.now)
    def __str__(self):
        return self.title

choice=[
    ('Applied','Applied'),
    ('Under Review','Under Review'),
    ('Shortlisted','Shortlisted'),
    ('Selected','Selected'),
    ('Rejected','Rejected')
]
class tbl_apply(models.Model):
    user=models.ForeignKey(tbl_register,on_delete=models.CASCADE)
    job=models.ForeignKey(tbl_job,on_delete=models.CASCADE)
    date=models.DateTimeField(null=True,auto_now_add=True)
    remark=models.TextField(null=True)
    status=models.CharField(max_length=50,null=True,
                            choices=choice,default='Applied')

