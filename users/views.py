from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404

from .forms import SignUpForm
from .models import MyUser


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            # load the profile instance created by the signal
            user.save()
            raw_password = form.cleaned_data.get('password1')

            cartUser = MyUser.objects.create(user=user)
            # login user after signing up
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            # redirect user to home page
            # player = MyUser.objects.get_or_create(user=user)
            return redirect(personal_view)
    else:
        form = SignUpForm()
    return render(request, 'register/register.html', {'form': form})


def personal_view(request):
    if request.user.is_authenticated:
        obj = get_object_or_404(User, username=request.user)
        context = {
            'username': obj.username,
            'name': obj.first_name+" "+obj.last_name,
            'order_history': obj.myuser.order_history,
            'cart': obj.myuser.cart,
        }
        return render(request, "personal.html", context)
    else:
        return render(request, "not_logged_in/not_logged_in.html", {})
