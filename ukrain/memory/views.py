from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import *

# Create your views here.
class MainView(View):
    def get(self,request):
        return render(request,'main.html')

class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context=context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))


class LoginView(View):
    def get(self, request):
        form = UserLoginForm()
        context = {'form': form}
        return render(request, 'login.html', context=context)

    def post(self, request):
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return HttpResponseRedirect(reverse_lazy('main'))
        context = {'form': form}
        return render(request, 'login.html', context=context)


class LogoutView(View):
    def get(self, request):
        auth.logout(request)
        return redirect(reverse_lazy('main'))


class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        context = {'form': form}
        return render(request, 'register.html', context=context)

    def post(self, request):
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('login'))


class AddReviewView(View):
    def get(self,request):
        form = ReviewForm
        context = {'form':form}
        return render(request,'review.html',context=context)

    def post(self,request):
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.author_id = request.user.id
            review.save()
            return HttpResponseRedirect(reverse_lazy('main'))

class ReviewListView(View):
    def get(self,request):
        review = Review.objects.all()
        context = {'review':review}
        return render(request,'review_list.html', context=context)