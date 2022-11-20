# from django.contrib.auth.models import User
# from django.contrib.auth.mixins import UserPassesTestMixin
from multiprocessing import context
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView, DetailView
from .models import Sbj, Tmt, Atd
from account.models import User
from .program import ser, create

# ログインしたユーザだけ
class myroll(TemplateView, LoginRequiredMixin):
    template_name = 'myroll/top.html'
    # create.create()

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super().get_context_data(**kwargs)
        context['user'] = user

        for_range10 = [i for i in range(10)]
        context['for_range10'] = for_range10

        # atend = Atd.objects.get(std_id = user.std_id)
        sbj_list = Sbj.objects.filter(std_fac=(user.std_fac or "ALL"), std_grd=user.std_grd)
        list = [["", 0, 0]]
        #  = [["数学ⅡA", 5, 16], ["数学ⅡB", 5, 16], ["体育", 5, 16], ["創造製作", 4, 16]]
        now_count = Atd.objects.filter(std_id=user.std_id)
        for sbj in sbj_list:
            for count in now_count:
                if sbj.sbj_name == count.sbj_name:
                    list.append([sbj.sbj_name, count.atd_time, sbj.curr_cnt, sbj.total_cnt])
                    break

        list.remove(["", 0, 0])
        context['subjects'] = list

        # if ((sub.count / sub.total) <= 1):
        #     context['warning'] = atend.subject

        test = Sbj.objects.raw('SELECT * FROM myroll_sbj WHERE std_grd=2')
        for t in test:
            context['test'] = t

        return context


class subjectView(TemplateView):
    template_name = 'myroll/subject.html'

    def get_context_data(self, **kwargs):
        return super().get_context_data(**kwargs)


class scheduleView(TemplateView):
    template_name = 'myroll/schedule.html'

    def get_context_data(self, **kwargs):
        user = self.request.user

        context = super().get_context_data(**kwargs)

        context['user'] = user
        # atend = Attending.objects.get(userpk = user.pk)
        context['subject'] = ["歴史", "数学", "体育", "哲学"]
        # atend.subject
        return context

class receptionView(TemplateView):
    template_name = 'myroll/reception.html'

    def get_context_data(self, **kwargs):
        # ser.
        context = super().get_context_data(**kwargs)
        context["result"] = "success"
        return context

    def post(self, **kwargs):
        self.request
