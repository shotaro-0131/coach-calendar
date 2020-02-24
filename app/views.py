from django.shortcuts import render, redirect
from .forms import SignUpForm
from . import mixins
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(
    LoginView, LogoutView
)
from . forms import LoginForm, MenuForm
from django.views.decorators.csrf import ensure_csrf_cookie
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
# Create your views here.
@ensure_csrf_cookie 
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'signup.html', context)
def index(request):
    return render(request, 'month.html', {'user_name': "村田"})


class CreatMenu(generic.CreateView, mixins.MonthCalendarMixin):
    form_class = MenuForm
    
@method_decorator(login_required , name="dispatch")
class MonthCalendar(mixins.MonthCalendarMixin, mixins.PlanMixin, generic.FormView):
    """月間カレンダーを表示するビュー"""
    template_name = 'month.html'
    form_class = MenuForm
    status_code = 200
    
    success_url = 'month'

    def post(self, request, **kwargs):
        print('kore',request.session)
        if request.method == 'POST':
            form_class = MenuForm(request.POST)

            form_class.is_valid()
            form_class.save()
            context = super().get_context_data(**kwargs)
            calendar_context = self.get_month_calendar()
            context.update(calendar_context)
            return redirect('month')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        plans = self.get_plan(calendar_context)
        print("ii",plans)

        context.update(calendar_context)
        context.update(plans)
        return context
    # def dispatch(self, *args, **kwargs):
    #     return redirect('login')

class Planing(mixins.AdminCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'month.html'

    def get_context_data(self, **kwargs):
        self.create_menu()
        context = super().get_context_data(**kwargs)
        calendar_context = super().get_month_calendar()
        context.update(calendar_context)
        return context
 
class Login(LoginView):
    #ログインページ
    form_class = LoginForm
    template_name = 'login.html'
 
 
class Logout(LoginRequiredMixin, LogoutView):
    #ログアウトページ
    template_name = 'login.html'
 
 
# def logout(request):
#     return render(request, 'login.html')