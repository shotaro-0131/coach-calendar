from django.shortcuts import render, redirect
from .forms import SignUpForm
from . import mixins
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import(
    LoginView, LogoutView
)
from . forms import LoginForm


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

class MonthCalendar(mixins.MonthCalendarMixin, generic.TemplateView):
    """月間カレンダーを表示するビュー"""
    template_name = 'month.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        calendar_context = self.get_month_calendar()
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