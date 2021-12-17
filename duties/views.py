import calendar
import json
from typing import Dict, Union, List

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.cache import cache_page

from . import models
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
# @cache_page(60 * 15)
def get_user_duties(request, username):
    user = models.Profile.objects.get(user__username=username)
    duties = [str(duty) for duty in user.duties.all()]

    return HttpResponse(json.dumps(duties))


@login_required
def get_users(request, username: str):
    if username:
        result = models.Profile.objects.get(user__username=username)
    else:
        result = models.Profile.objects.all()

    data = serializers.serialize('json', result.duties.all())

    return HttpResponse(data)


@login_required
def calendar_view(request):
    calendar_data = generate_calendar([2021])
    weekheader = calendar.weekheader(3).split()
    persons = models.Profile.objects.all()
    groups = models.Group.objects.all().order_by('name')

    payload = {
        'calendar': calendar_data,
        'weekheader': weekheader,
        'persons': persons,
        'groups': groups,
    }

    return render(request, 'duties/calendar.html', payload)


def logout_view(request):
    logout(request)
    return redirect('duties:login')
