from django.contrib import admin
from .models import *

# Register your models here.

class tblcontactAdmin(admin.ModelAdmin):
    list_display=("id","name","email","mobile","message")
admin.site.register(tblcontact,tblcontactAdmin)

class tblgalleryAdmin(admin.ModelAdmin):
    list_display=("id","title","picture")
admin.site.register(tblgallery,tblgalleryAdmin)    

class tblteamAdmin(admin.ModelAdmin):
    list_display=("id","name","designation","picture")
admin.site.register(tblteam,tblteamAdmin)   

class tbl_registerAdmin(admin.ModelAdmin):
    list_display=("name","email","mobile","password","address","profile_picture","gender","dob","skills","education","experience","resume")
admin.site.register(tbl_register,tbl_registerAdmin)    

class tbl_categoryAdmin(admin.ModelAdmin):
    list_display=("id","name","icon")
admin.site.register(tbl_category,tbl_categoryAdmin)    


class tbl_cityAdmin(admin.ModelAdmin):
    list_display=("id","name","icon","state","country")
admin.site.register(tbl_city,tbl_cityAdmin)    


class tbl_companyAdmin(admin.ModelAdmin):
    list_display=("id","name","logo","email","mobile","address","owner","hr","hrcontact","city")
admin.site.register(tbl_company,tbl_companyAdmin)    


class tbl_jobAdmin(admin.ModelAdmin):
    list_display=("id","title","company","category","city","detail","salary","experience","vacancy","lastdate","jobtype","posted_on")
admin.site.register(tbl_job,tbl_jobAdmin)    


class tbl_applyAdmin(admin.ModelAdmin):
    list_display=("id","user","job","date","remark","status")
admin.site.register(tbl_apply,tbl_applyAdmin)    