from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def myroll(request):
    for_range10 = [i for i in range(10)]

    return render(request, 'myroll/index.html', {'for_range10': for_range10})


# def signup(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data.get('username')
#             raw_password = form.cleaned_data.get('password1')
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('myroll')
#     else:
#         form = UserCreationForm()
#     return render(request, 'registration/signup.html', {'form': form})
