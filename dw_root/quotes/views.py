from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils import timezone

from datetime import datetime, timedelta

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
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except Exception:
                pass
            quote.save()
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
    success_url = reverse_lazy('customer-list')

# def quote_delete(request, id):
#     context = {}

#     obj = get_object_or_404(Customer, id=id)

#     if request.method == "POST":
#         obj.delete()
#         return HttpResponseRedirect("/")

#     return render(request, 'quotes/quote_delete.html', context)


class CustomerUpdateView(UpdateView):
    model = Customer
    fields = '__all__'
    template_name_suffix = '_update'
    # success_url = 'detail/'


"""Список сертификатов"""


class SignList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = DigitalSign
    template_name = 'quotes/sign_list.html'
    queryset = DigitalSign.objects.all()

    def get_context_data(self, **kwargs):

        context = super(SignList, self).get_context_data(**kwargs)
        current_time = timezone.now()
        time_15days = current_time + timedelta(days=15)
        context.update({
            'active_signs': DigitalSign.objects.filter(end_date__gte=current_time),
            'signs_15days_left': DigitalSign.objects.filter(end_date__range=[current_time, time_15days])
        })
        return context

