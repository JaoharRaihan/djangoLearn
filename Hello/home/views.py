from django.shortcuts import render,HttpResponse
def index(request):
    context = {
        "variable1":"This is sent",
        "variable2":"fucking"
    }
    return render(request,'index.html',context)
    # return HttpResponse("This is homepage")
def about(request):
    # return HttpResponse("This is about")
        return render(request,'about.html',context)
def contract(request):
    # return HttpResponse("This is contract")
        return render(request,'contract.html',context)
def Photos(request):
    # return HttpResponse("This is Photos")
        return render(request,'Photos.html',context)