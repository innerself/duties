from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import LoginForm
from .utils import DutyCalendar


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
        form = LoginForm()

    return render(request, 'duties/login.html', {'form': form})


def calendar(request):
    calendar_ = DutyCalendar().draw_calendar(2021)
    return render(request, 'duties/calendar.html', {'calendar': calendar_})


def logout_view(request):
    logout(request)
    return redirect('duties:login')
