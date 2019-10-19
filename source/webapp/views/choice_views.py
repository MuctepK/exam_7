from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import UpdateView, DeleteView, CreateView

from webapp.forms import ChoiceForm
from webapp.models import Choice, Poll


class ChoiceCreateView(CreateView):
    template_name = 'create.html'
    form_class = ChoiceForm
    model = Choice
    extra_context = {'title': 'Создание варианта ответа'}

    def dispatch(self, request, *args, **kwargs):
        self.poll = self.get_article()
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        self.poll.choices.create(**form.cleaned_data)
        return redirect('view_poll', pk=self.poll.pk)

    def get_article(self):
        poll_pk = self.kwargs.get('pk')
        print(poll_pk)
        return get_object_or_404(Poll, pk=poll_pk)


class ChoiceUpdateView(UpdateView):
    template_name = 'update.html'
    form_class = ChoiceForm
    model = Choice
    extra_context = {'title': 'Обновление варианта ответа'}

    def get_success_url(self):
        return reverse('view_poll', kwargs={'pk': self.object.poll.pk})


class ChoiceDeleteView(DeleteView):
    template_name = 'delete.html'
    model = Choice
    extra_context = {'title': 'вариант ответа '}

    def get_success_url(self):
        return reverse('view_poll', kwargs={'pk': self.object.poll.pk})