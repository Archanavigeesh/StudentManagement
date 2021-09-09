from django.shortcuts import render,redirect
from . models import *

def fnlogin(request):
    try:
        if request.method=="POST":
            username=request.POST.get('username')
            password=request.POST.get('password')
            loginobj=Login.objects.get(username=username,password=password)
            usertype=loginobj.usertype
            if loginobj and usertype=='Admin':
                request.session['id']=loginobj.id
                return redirect('adminhome')
            elif loginobj and usertype=='User':
                request.session['id']=loginobj.id
                return redirect('stdhome') 
    except Exception as e:
        return render(request,'login.html')
    return render(request,'login.html')
def fnadminstdreg(request):
    try:
        if request.session['id'] :
            if request.method=="POST":
                name=request.POST.get('name')
                contact=request.POST.get('contact')
                email=request.POST.get('email')
                username=request.POST.get('username')
                password=request.POST.get('password')
                usertype="User"
                loginobj=Login(username=username,password=password,usertype=usertype)
                loginobj.save()
                stdobj=Student(user=loginobj,name=name,contact=contact,email=email)
                stdobj.save()
                state="Active"
                stateobj=State(stdlogin=loginobj,std=stdobj,state=state)
                stateobj.save()
                #return redirect('login')
            return render(request,'adminstdreg.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnstudentregistration(request):
            if request.method=="POST":
                name=request.POST.get('name')
                contact=request.POST.get('contact')
                email=request.POST.get('email')
                username=request.POST.get('username')
                password=request.POST.get('password')
                usertype="User"
                loginobj=Login(username=username,password=password,usertype=usertype)
                loginobj.save()
                stdobj=Student(user=loginobj,name=name,contact=contact,email=email)
                stdobj.save()
                state="Active"
                stateobj=State(stdlogin=loginobj,std=stdobj,state=state)
                stateobj.save()
                return redirect('login')
            return render(request,'stdreg.html')
def fnadminhome(request):
    try:
        if request.session['id']:
            return render(request,'adminhome.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fninactivestd(request):
    try:
        if request.session['id']:
            inactive=State.objects.filter(state="Inactive")
            loginobj=Login.objects.all()
            if inactive:
                return render(request,'inactive.html',{'inactive':inactive})
            return render(request,'inactive.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnactivestd(request):
    try:
        if request.session['id']:
            active=State.objects.filter(state="Active")
            loginobj=Login.objects.all()
            if active:
                return render(request,'active.html',{'active':active})
            return render(request,'active.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnstdhome(request):
    try:
        if request.session['id']:
            logid=request.session['id']
            stdobj=Student.objects.get(user=logid)
            return render(request,'stdhome.html',{'std':stdobj})
        else:
            return render(request,'login.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnstdupdate(request):
    try:
        if request.session['id']:
            logid=request.session['id']
            stdobj=Student.objects.get(user=logid)
            logobj=Login.objects.get(id=logid)
            stateobj=State.objects.get(stdlogin=logid)
            if request.method=="POST":
                name=request.POST.get('name')
                contact=request.POST.get('contact')
                email=request.POST.get('email')
                username=request.POST.get('username')
                password=request.POST.get('password')
                stdobj.name=name
                stdobj.contact=contact
                stdobj.email=email
                stdobj.save()
                logobj.username=username
                logobj.password=password
                logobj.save()
                return render(request,'update.html',{'std':stdobj,'state':stateobj})
            return render(request,'update.html',{'std':stdobj,'state':stateobj})
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnchangestate(request):
    try:
        if request.session['id']:
            val=int(request.POST.get('btn'))
            stateobj=State.objects.get(id=val)
            state=stateobj.state
            if state=="Active":
                stateobj.state="Inactive"
                stateobj.save()
                active=State.objects.filter(state="Active")
                if active:
                    return render(request,'active.html',{'active':active})
                else:
                    return render(request,'active.html')
            elif state=="Inactive":
                stateobj.state="Active"
                stateobj.save()
                inactive=State.objects.filter(state="Inactive")
                if inactive:
                    return render(request,'inactive.html',{'inactive':inactive})
                else:
                    return render(request,'inactive.html')
            return render(request,'adminhome.html')
    except Exception as e:
        return redirect('login')
    return redirect('login')
def fnlogout(request):
    try:
        if request.session['id']:
            del request.session['id']
            return redirect('login')
    except Exception as e:
        return redirect('login')
    return redirect('login')
