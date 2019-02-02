from django.shortcuts import render , HttpResponse , redirect
from .forms import UserRegisterForm , UserUpdateForm , ProfileUpdateForm , UserChangePassword
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.views.generic import CreateView
from django.contrib.auth import update_session_auth_hash
from django.http.request import HttpRequest

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            print(username)
            return redirect('home')
        else:
            return HttpResponse("not valid")
    else:
        form = UserRegisterForm()
        return render(request, "register.html" , {"title" : "Register" , "form" : form})


@login_required
def profile(request):
    if request.method == "POST":
        profile_form = UserUpdateForm(request.POST ,instance=request.user)
        profile_image_form = ProfileUpdateForm(request.POST , request.FILES , instance=request.user.profile)
        if profile_form.is_valid() and profile_image_form.is_valid():
            profile_form.save()
            profile_image_form.save()
            messages.success(request, "Profile Updated successfully")
            return redirect('profile')
        else:
            if not profile_form.is_valid():
                messages.warning(request, "Username or email not correct")
                return redirect('profile')
            elif not profile_image_form.is_valid():
                messages.warning(request, "Profile image not correct")
                return redirect('profile')
            else:
                return redirect("profile")
    else:
        profile_form = UserUpdateForm(instance=request.user)
        profile_image_form = ProfileUpdateForm(instance=request.user.profile)
        context = {
            'profile_form' : profile_form,
            "profile_image_form" : profile_image_form,

        }
        return render(request , 'profile.html' , context)


@login_required
def change_password(request):
    if request.method == 'POST':
        form = UserChangePassword( request.POST)
        print(form.errors)
        print(form.error_messages)
        print(form.error_class)
        if form.is_valid():
            print(form.errors)
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('profile')
        else:
            messages.warning(request, 'Your older password is incorrect, enter again!')
            return redirect('changepassword')


    else:
        form = UserChangePassword(request.user)
        print(form.errors)
        print(form.error_messages)
        print(form.error_class)
        print('hello')
        return render(request, 'change_password.html', {'form': form})


