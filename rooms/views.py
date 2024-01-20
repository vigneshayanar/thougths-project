from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from .models import Room
# Create your views here.


@login_required
def rooms(request):
    rooms=Room.objects.all()

    return render(request,'room/rooms.html',{'rooms':rooms})

def join(request,pk):
    rooms=Room.objects.get(id=pk)
    if request.method=="POST":
        new_desc=request.POST.get('desc')
        if new_desc:
            if rooms.desc:
                rooms.descp+=f"\n{new_desc}"
            else:
                rooms.descp=new_desc
            rooms.save()
        return redirect(request.path)

        
    return render(request,'room/join.html',{'rooms':rooms})