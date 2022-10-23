# from django.contrib.auth.models import User
# from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView

# @login_required
# def myroll(request):
#     for_range10 = [i for i in range(10)]

#     return render(request, 'myroll/top.html', {'for_range10': for_range10})

# class OnlyYouMixin(UserPassesTestMixin):
#     raise_exception = True

#     def test_func(self):
#         # 今ログインしてるユーザーのpkと、そのマイページのpkが同じなら許可
#         user = self.request.user
#         return user.pk == self.kwargs['pk']

# class myroll(OnlyYouMixin, DetailView):
#     model = User
#     template_name = 'myroll/top.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         for_range10 = [i for i in range(10)]
#         context['for_range10'] = for_range10
#         context['subjects'] = [["国語", "あ"], ["数学", "い"], ["理科", "う"], ["社会", "う"], ["英語", "お"]]
#         return context


# ログインしたユーザだけ
class myroll(TemplateView, LoginRequiredMixin):
    template_name = 'myroll/top.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super().get_context_data(**kwargs)
        context['user'] = user

        for_range10 = [i for i in range(10)]
        context['for_range10'] = for_range10

        context['subjects'] = [["国語", "あ"], ["数学", "い"], ["理科", "う"], ["社会", "う"], ["英語", "お"]]
        return context

# index = myroll.as_view() 一旦消しとく


class subjectView(TemplateView):
    template_name = 'myroll/subject.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


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
