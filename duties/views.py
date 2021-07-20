import calendar

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import LoginForm
from .utils import generate_calendar


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['login']
            password = form.cleaned_data['password']
            user = authenticate(
                request=request,
                username=username,
                password=password,
            )

            if user is not None:
                login(request, user)
                return redirect('duties:calendar')
            else:
                print()
    else:
        if request.user.is_authenticated:
            return redirect('duties:calendar')
        form = LoginForm()

    return render(request, 'duties/login.html', {'form': form})


@login_required
def calendar_view(request):
    calendar_data = generate_calendar([2021])
    weekheader = calendar.weekheader(3).split()

    payload = {
        'calendar': calendar_data,
        'weekheader': weekheader,
    }

    return render(request, 'duties/calendar.html', payload)


def logout_view(request):
    logout(request)
    return redirect('duties:login')
