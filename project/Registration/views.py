from django.shortcuts import render
from email import message
from django.http import HttpResponse
from . models import Employeeinfo

# Create your views here.
def index(request):
    return render(request,'index.html')

def success_regis(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('password')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        address=request.POST.get('address')
        city=request.POST.get('city')
        state=request.POST.get('state')
        pincode=request.POST.get('pin')
        country=request.POST.get('country')
        company=request.POST.get('company')
        occupation=request.POST.get('occupation')
        experience=request.POST.get('experience')
        

        if Employeeinfo.objects.filter(username=username).exists() and Employeeinfo.objects.filter(email=email).exists():
            return HttpResponse("Username / Email ID already exsists ! Please try another !")
        
        obj=Employeeinfo()
        obj.username=username
        obj.password=password
        obj.email=email
        obj.phone=phone
        obj.address=address
        obj.city=city
        obj.state=state
        obj.pincode=pincode
        obj.country=country
        obj.company=company
        obj.occupation=occupation
        obj.experience=experience
        obj.save()

        return render(request,'success_regis.html')
    else:

        return render(request,'signup.html')

def login(request):

    return render(request,'login.html')

def success_login(request):
    if(request.method=='POST'):
            username = request.POST.get('uname')
            password = request.POST.get('password')
            if(Employeeinfo.objects.filter(username=username).exists() and Employeeinfo.objects.filter(password=password).exists()):
                request.session['abc']=username
                return render(request,'success_login.html')
            else:
                message.Message.info(request,'Invalid credentials!!')
                return render(request,'login.html')

def view(request):
    a=Employeeinfo.objects.all()
    context={'data':a}
    return render(request,'view.html',context)