from django.views.generic import ListView, DetailView

from webapp.models import Poll


class PollListView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']


class PollDetailView(DetailView):
    template_name = 'poll/poll.html'
    model = Poll
    context_object_name = 'poll'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        poll = self.object
        choices = poll.choices.all()
        context['choices'] = choices
        return context

