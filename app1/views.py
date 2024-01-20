from django.shortcuts import render,redirect
from .froms import siginupform
from django.contrib.auth import login
# Create your views here.
def frontpage(request):
    return render(request,'app1/frontpage.html')


def siginup(request):
    if request.method=='POST':
        form=siginupform(request.POST)

        if form.is_valid():
            user= form.save()
            login(request,user)
            
            return redirect('fronpage')
    else:
        form=siginupform()
        
    return render(request,'app1/signup.html',{'form':form})