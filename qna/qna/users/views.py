from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django.views.generic import DetailView, RedirectView, UpdateView

from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.http import HttpResponse

from django.urls import reverse
from django.db.models import Q
from django.shortcuts import render, redirect
from django.contrib.auth import logout, authenticate, login
from . import forms, models

User = get_user_model()


def register(request):
    if request.method == 'GET':
        form = forms.RegistrationForm()
        return render(request, 'users/register.html', {'form': form})
    
    elif request.method == 'POST':
        form = forms.RegistrationForm(request.POST)
        if form.is_valid():
            form.save()

            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            print(username, password)
            
            # 가입후 자동 로그인
            user=authenticate(request, username=username, password=password)
            if user is not None :
                login(request, user, backend='django.contrib.auth.backends.ModelBackend')
                print('로그인')
                return redirect(reverse('curation:main'))
            else :
                print('로그인 실패')
                return redirect(reverse('users:register'))

        return HttpResponse(status=405)
        


def user_login(request):
    if request.method=='GET':
        return render(request, 'users/login.html')
    
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request, username=username, password=password)
        user = User.objects.get(username=username)
        user_type = user.user_type.userType
        print(user_type)
        
        if user is not None :
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            print('로그인')
            return HttpResponseRedirect(reverse('curation:main'))
        else :
            print('로그인 실패')
            return HttpResponseRedirect(reverse('curation:main'))
        
def user_logout(request):
    logout(request)
    # Perform any additional actions after logout if needed
    # For example, you can redirect the user to a specific page or display a success message
    return redirect(reverse('curation:main'))         

class UserDetailView(LoginRequiredMixin, DetailView):
    model = User
    slug_field = "username"
    slug_url_kwarg = "username"
user_detail_view = UserDetailView.as_view()


class UserUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = User
    fields = ["name"]
    success_message = _("Information successfully updated")

    def get_success_url(self):
        assert self.request.user.is_authenticated  # for mypy to know that the user is authenticated
        return self.request.user.get_absolute_url()

    def get_object(self):
        return self.request.user


user_update_view = UserUpdateView.as_view()


class UserRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("users:detail", kwargs={"username": self.request.user.username})


user_redirect_view = UserRedirectView.as_view()
