from django.shortcuts import redirect, render
from users.forms import ProfileUpdateForm, UserRegistrationForm, UserUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from warehouses.models import Warehouses


def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(
                request, f" {username}, your account has been created successfully")
            return redirect("home")
    else:
        form = UserRegistrationForm()

    return render(request, "users/register.html", {'form': form})


def home(request):
    warehouses = Warehouses.objects.all()

    return render(request, "warehouses/warehouses.html",{'warehouses': warehouses})


@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.profile,)

        if p_form.is_valid() and u_form.is_valid():
            p_form.save()
            u_form.save()
            messages.success(
                request, f" your account has been updated successfully")
            return redirect("profile")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, "users/profile.html", context)
