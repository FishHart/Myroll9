# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required

from django.views.generic import TemplateView

# @login_required
# def myroll(request):
#     for_range10 = [i for i in range(10)]

#     return render(request, 'myroll/top.html', {'for_range10': for_range10})

class myroll(TemplateView):
    template_name = 'myroll/top.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        for_range10 = [i for i in range(10)]
        context['for_range10'] = for_range10
        context['subjects'] = [["国語", "あ"], ["数学", "い"], ["理科", "う"], ["社会", "う"], ["英語", "お"]]
        return context

# index = myroll.as_view()


class subjectView(TemplateView):
    template_name = 'myroll/subject.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)



# @管理者だけ
class scheduleView(TemplateView):
    template_name = 'myroll/schedule.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


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
