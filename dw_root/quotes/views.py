from django.shortcuts import get_object_or_404, redirect, render
from django.http import HttpResponseRedirect, request
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.base import View
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Quote
from .forms import QuoteForm
from pages.models import Page


class QuoteList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    context_object_name = 'all_quotes'

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(QuoteList, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context


"""Регистрация записи"""


@login_required(login_url=reverse_lazy('login'))
def quote_req(request):
    submitted = False
    if request.method == 'POST':
        form = QuoteForm(request.POST, request.FILES)

        if form.is_valid():
            quote = form.save(commit=False)
            try:
                quote.username = request.user
            except Exception:
                pass
            quote.save()
            return HttpResponseRedirect('/quote/?submitted=True')
    else:
        form = QuoteForm()
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'quotes/quote.html', {'form': form,
                                                'page_list': Page.objects.all(),
                                                'submitted': submitted})


class QuoteView(LoginRequiredMixin, DetailView):
    login_url = reverse_lazy('login')
    context_object_name = 'quote'

    def get_queryset(self):
        return Quote.objects.filter(username=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(QuoteView, self).get_context_data(**kwargs)
        context['page_list'] = Page.objects.all()
        return context

class Register(CreateView):
    """Создание формы регистрации пользователей."""

    template_name = 'registration/register.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('register-success')

    def form_valid(self, form):
        form.save()
        return HttpResponseRedirect(self.success_url)


"""Удаление записи"""
def quote_delete(request, id):
    context = {}

    obj = get_object_or_404(Quote, id=id)

    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/")

    return render(request, 'quotes/quote_delete.html', context)

