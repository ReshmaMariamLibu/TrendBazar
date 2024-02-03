from django.shortcuts import render,redirect
from django.views.generic import View,CreateView,TemplateView,FormView,ListView
from vendor.forms import UserForm,LoginForm,CategoryForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from api.models import Category



class SignUpView(CreateView):
    template_name="register.html"
    form_class=UserForm

    def get_success_url(self):
        return reverse("signin")
    

class SignInView(FormView):
      template_name="login.html"
      form_class=LoginForm 

      def post(self,request,*args,**kwargs):
           form=LoginForm(request.POST)
           if form.is_valid():
                uname=form.cleaned_data.get("username")
                pwd=form.cleaned_data.get("password")
                user_object=authenticate(request,username=uname,password=pwd)
                if user_object:
                     login(request,user_object)
                     print("logged in successfully.....")
                     return redirect("index")
                
           print("failed...")
           messages.error(request,"failed to login invalid credentials")
           return render(request,"login.html",{"form":form}) 
      




class IndexView(CreateView,ListView):
     template_name="index.html"
     form_class=CategoryForm
     model=Category
     def form_valid(self,form): 
          form.instance.user=self.request.user
          return super().form_valid(form) 
     def get_success_url(self): 
          return reverse("index")
     
          
     
     
     

class SignOutView(View):
     def get(self,request,*args,**kwargs):
          logout(request)
          return redirect("signin")
    








