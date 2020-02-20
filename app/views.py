from django.shortcuts import render, redirect
from .forms import SignUpForm
from . import mixins
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(
    LoginView, LogoutView
)
from . forms import LoginForm, MenuForm


from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
 
class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = SignUpForm()

    context = {'form':form}
    return render(request, 'signup.html', context)
def index(request):
    return render(request, 'month.html', {'user_name': "村田"})

class MonthCalendar(mixins.MonthCalendarMixin, mixins.PlanMixin, generic.FormView):
    """月間カレンダーを表示するビュー"""
    template_name = 'month.html'
    form_class = MenuForm
    

    status_code = 200
    
    success_url = 'index'
    def post(self, request, **kwargs):
        if request.method == 'POST':
            form_class = MenuForm(request.POST)

            form_class.is_valid()
            print("aa")
            form_class.save()
            context = super().get_context_data(**kwargs)
            calendar_context = self.get_month_calendar()
            context.update(calendar_context)
            return render(request,'index.html',context)
   
        # new logic!
            # template_name.save()

    def get_context_data(self, **kwargs):
        print('33')
        # print(all_entries,"1")
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
        plans = self.get_plan(calendar_context)

        print(plans)
        context.update(calendar_context)
        context.update(plans)
        return context

class Planing(mixins.AdminCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'month.html'

    def get_context_data(self, **kwargs):
        print('22')
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
 
 
# def index(request):
    
#     return render(request, 'accounts/index.html')