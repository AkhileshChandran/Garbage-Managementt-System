from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,FormView,TemplateView
from my_work.forms import UserForm,GarbageBinForm
from my_work.models import User,GarbageBin
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from my_work.forms import CustomAuthenticationForm
from django.contrib.auth import authenticate,login,logout



# Create your views here.


class HomePage(TemplateView):
    template_name="registration/home.html"




class AddUser(View):
    def get(self,request,*args,**kwargs):
        form=UserForm()
        return render(request,"registration/user.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form=UserForm(request.POST)
        if form.is_valid():
            User.objects.create_user(**form.cleaned_data)
            return render(request,"registration/user.html",{"form":form})



class CustomLoginView(LoginView):
    template_name = 'registration/login.html'  
    success_url = 'your_success_url'

    def form_valid(self, form):
        user = form.get_user()
        login(self.request, user)
        if user.user_type == 'admin':
            return redirect('home_1')  
        elif user.user_type == 'customer':
            return redirect('home_2')  
        elif user.user_type == 'driver':
            return redirect('home_3')  
        else:
            return redirect(self.success_url)
        


class CreateGarbage(View):
    def get(self,request,*args,**kwargs):
        form=GarbageBinForm()
        return render(request,"registration/garbage_create.html",{"form":form})
    
    def post(self,request,*args,**kwargs):
        form = GarbageBinForm(request.POST)
        if form.is_valid():
                GarbageBin.objects.create(**form.cleaned_data)
                return render(request,"registration/garbage_create.html",{"form":form})
        

class UpdateBin(View):
    def get(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        data = GarbageBin.objects.get(id=id)
        form = GarbageBinForm(instance=data)
        return render(request,"registration/garbage_update.html",{"form":form})
    

    def post(self,request,*args,**kwargs):
        id = kwargs.get("pk")
        data = GarbageBin.objects.get(id=id)
        form = GarbageBinForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect("home_1")
        

class DeleteBin(View):
     def get(self,request,*args,**kwargs):
          id = kwargs.get("pk")
          data = GarbageBin.objects.get(id=id).delete()
          return redirect("home_1")
     



class UsersList(View):
    def get(self, request, *args, **kwargs):
        data = User.objects.filter(user_type='customer')
        return render(request, "public/userlist.html", {"data": data})





    
                
