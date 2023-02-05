from django.shortcuts import render,HttpResponse
def index(request):
    return render(request,'index.html')
    # return HttpResponse("This is homepage")
def about(request):
    return HttpResponse("This is about")
def services(request):
    return HttpResponse("This is services")
def contract(request):
    return HttpResponse("This is contract")