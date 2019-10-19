from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from webapp.forms import PollForm, ChoiceForm
from webapp.models import Poll


class PollListView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']
    paginate_by = 5
    paginate_orphans = 0
    page_kwarg = 'page'


class PollDetailView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        choices = poll.choices.all()
        context['choices'] = choices
        context['form'] = ChoiceForm
        return context


class PollCreateView(CreateView):
    template_name = 'create.html'
    form_class = PollForm
    model = Poll
    extra_context = {'title': 'Создание опроса'}

    def get_success_url(self):
        return reverse('view_poll', kwargs={'pk': self.object.pk})


class PollUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = PollForm
    model = Poll
    extra_context = {'title': 'Обновление опроса'}

    def get_success_url(self):
        return reverse('view_poll', kwargs={'pk': self.object.pk})


class PollDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Poll
    extra_context = {'title': 'опрос '}
    success_url = reverse_lazy('index')
