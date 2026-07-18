
from .models import Chai_Varity
# Create your views here.
from django.shortcuts import render
from django.shortcuts import get_object_or_404

def all_chai(request):
    chais = Chai_Varity.objects.all()
    return render(request, 'all_chai.html',{'chais':chais})
def chai_detail(request,chai_id):
    chai = get_object_or_404(Chai_Varity,pk = chai_id)
    return render(request, 'chai_detail.html',{"chai":chai})
def certificate(request,chai_id):
    chai = get_object_or_404(Chai_Varity,pk = chai_id)
    return render(request, 'Certificate_chai.html',{"chai":chai})