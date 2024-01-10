from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from service.models import Contact
from service.models import Department
from service.models import DoctorDetails

def indexPage(request):
        data=Department.objects.all().values()
        print(data)
        return render(request,'index.html',{'departmentdata':data})

def aboutPage(request):
        return render(request,'about.html')

def servicePage(request):
        return render(request,'service.html')




def contactPage(request):
        # print(request)
        msg=''
        try:
                if request.method=="POST":
                        f_name=request.POST['name']
                        email=request.POST['email']
                        subject=request.POST['subject']
                        phone=request.POST['phone']
                        message=request.POST['message']
                        data=Contact(full_name=f_name,email_id=email,subject=subject,mob_num=phone,message=message)
                        data.save()
                        msg="Contact Data Send Successfully! "
        except:
                pass
        return render(request,'contact.html',{'message':msg})

def departmentPage(request):
        data=Department.objects.all().values()
        # print(data)
        contextData=[]
        for d in data:
                obj={}
                # print(d['id'])
                obj['id']=d['id']
                obj['department_name']=d['department_name']
                # print(obj)
                datad=DoctorDetails.objects.get(department_name_id=d['id'])
                # print(datad)
                dept_name=datad.__dict__
                # print(dept_name)
                obj['department_desc']=dept_name['department_desc']
                obj['d_id']=dept_name['id']
                contextData.append(obj)

 


        return render(request,'department.html',{'doctor_details':contextData})

def departmentSinglePage(request,id):
        # print(id)
        department_data=Department.objects.filter(id=id).values()
        # print(department_data)
        # print(department_data[0]['department_name'])
        contextData = []
        data=DoctorDetails.objects.filter(id=id).values()
        # print(data)
        obj = {}
        # d_id=data[0]['department_name_id']
        obj['department_desc']=data[0]['department_desc']
        obj['department_name']=department_data[0]['department_name']
        contextData.append(obj)
        # print(contextData)
        # print(contextData[0]['department_name'])
        return render(request,'department_single.html',{'doctor_details':contextData})


def appointmentPage(request,id):
        return render(request,'appointment.html')