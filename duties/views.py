from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import LoginForm


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            return HttpResponseRedirect('/thanks/')
    else:
        form = LoginForm()

    return render(request, 'duties/login.html', {'form': form})
