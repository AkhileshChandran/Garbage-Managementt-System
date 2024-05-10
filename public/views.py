from django.shortcuts import get_object_or_404, redirect, render
from django.views.generic import TemplateView,View
from public.forms import UserGarbageBinForm,ComplaintForm
from my_work.models import UserGarbageBin,Complaint
# Create your views here.



class HomePage(TemplateView):
    template_name="public/home.html"




class RequestBin(View):
    def get(self, request, *args, **kwargs):
        form = UserGarbageBinForm()
        return render(request, "public/bin_request.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = UserGarbageBinForm(request.POST)
        if form.is_valid():
            form.save()  # Save the form data to the database
            return render(request, "public/Home.html")
        else:
            return render(request, "public/bin_request.html", {"form": form})

class CustmoerComplaint(View):
    def get(self,request,*args,**kwargs):
        form = ComplaintForm()
        return render(request,"public/complaint.html",{"form":form}) 

    def post(self,request,*args,**kwargs):
        form = ComplaintForm(request.POST)
        if form.is_valid():
            Complaint.objects.create(**form.cleaned_data)
            return render(request,"public/complaint.html",{"form":form}) 
               




class PendingRequestsView(View):
    def get(self, request):
        pending_requests = UserGarbageBin.objects.filter(status='pending')
        return render(request, "public/pending_requests.html", {"pending_requests": pending_requests})

class AcceptRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'accepted'
        user_garbage_bin.save()
        return redirect('pending_requests')

class RejectRequestView(View):
    def post(self, request, pk):
        user_garbage_bin = get_object_or_404(UserGarbageBin, pk=pk)
        user_garbage_bin.status = 'rejected'
        user_garbage_bin.save()
        return redirect('pending_requests')
    
def pending_requests_view(request):
    pending_requests = UserGarbageBin.objects.filter(status='pending')
    return render(request, 'public/pending_requests.html', {'pending_requests': pending_requests})