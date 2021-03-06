from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, ModelFormMixin, UpdateView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone
from django_filters.views import FilterView

from datetime import timedelta

from .filters import SignFilter
from .models import Customer, DigitalSign
from .forms import CustomerForm, DigitalSignForm


"""Список пользователей"""


class CustomerList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerList, self).get_context_data(**kwargs)
        context.update({
            'end_date_sign': DigitalSign.end_date
        })
        return context


"""Добавление пользователя"""


@login_required(login_url=reverse_lazy('login'))
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = CustomerForm(request.POST, request.FILES)

        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except Exception:
                pass
            quote.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = CustomerForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'quotes/quote.html', {'form': form,
                                                 'submitted': submitted})


"""Добавление сертификата"""

@login_required(login_url=reverse_lazy('login'))
def sign_create(request):
    submitted = False
    if request.method == 'POST':
        form = DigitalSignForm(request.POST, request.FILES)

        if form.is_valid():
            sign = form.save(commit=False)
            try:
                sign.username = request.user
            except Exception:
                pass
            sign.save()
            form.save_m2m()
            return HttpResponseRedirect('/sign/create/?submitted=True')
    else:
        form = DigitalSignForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'quotes/sign_create.html', {'form': form,
                                                 'submitted': submitted})

"""Информация о пользователе"""


class CustomerDetailView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    model = Customer

    def get_context_data(self, **kwargs):
        context = super(CustomerDetailView, self).get_context_data(**kwargs)
        return context

    
"""Создание формы регистрации пользователей."""


class Register(CreateView):

    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


"""Удаление прользователя"""

class CustomerDeleteView(DeleteView):
    model = Customer
    success_url = reverse_lazy('customer_list')


"""Изменение пользователя"""

class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = 'customer_update'
    # success_url = 'detail/'


"""Список сертификатов"""

current_time = timezone.now()

class SignList(LoginRequiredMixin, FilterView):
    login_url = reverse_lazy('login')
    model = DigitalSign
    template_name = 'quotes/sign_list.html'
    queryset = DigitalSign.objects.filter(end_date__gte=current_time)
    filterset_class = SignFilter

    def get_context_data(self, **kwargs):

        context = super(SignList, self).get_context_data(**kwargs)
        left_7days = current_time + timedelta(days=7)
        left_15days = current_time + timedelta(days=15)
        left_30days = current_time + timedelta(days=30)
        context.update({
            # 'active_signs': DigitalSign.objects.filter(end_date__gte=current_time),
            'signs_7days_left': DigitalSign.objects.filter(end_date__range=[current_time, left_7days]),
            'signs_15days_left': DigitalSign.objects.filter(end_date__range=[left_7days, left_15days]),
            'signs_30days_left': DigitalSign.objects.filter(end_date__range=[left_15days, left_30days]),
        })
        return context

class Sign7DaysList(SignList):
    template_name = 'quotes/7days_left.html'

class Sign15DaysList(SignList):
    template_name = 'quotes/15days_left.html'

class Sign30DaysList(SignList, ListView):
    template_name = 'quotes/30days_left.html'



"""Изменение ЭП"""

class SignUpdateView(UpdateView, ModelFormMixin):
    model = DigitalSign
    form_class = DigitalSignForm
    template_name_suffix = '_update'


"""Удаление ЭП"""

class SignDeleteView(DeleteView):
    model = DigitalSign
    success_url = reverse_lazy('sign_list')
