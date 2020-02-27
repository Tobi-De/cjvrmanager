from django.shortcuts import render, redirect

from .forms import SignUp


def signup(request):
    if request.method == "POST":
        form = SignUp(request.POST)
        if form.is_valid():
            form.save()
            redirect('login')
    else:
        form = SignUp()
    return render(request, 'users/signup.html', {'form': form})
