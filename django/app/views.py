from django.shortcuts import render
from .models import Name
# Create your views here.
def index(request):
    names=Name.objects.all()
    return render(request,'index.html',{'names':names})