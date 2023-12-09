from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
    return render(request, "home.html")
def calculate(request):
    x=int(request.POST["t1"])
    y=int(request.POST["t2"])
    opt=request.POST["op"]
    result=" "
    if opt=="add":
        z=x+y
        result=result+"The sum is :" +str(z)

    elif opt=='sub':
        z=x-y
        result=result+"The difference is:" +str(z)
    elif opt=='mul':
        z=x*y
        result=result+"The mul is:" +str(z)

    else:
        z=x/y
        result=result+"ThE division is:"+str(z)
    return HttpResponse(result)

