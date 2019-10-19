from django.views.generic import ListView

from webapp.models import Poll


class PollListView(ListView):
    template_name = 'poll/index.html'
    model = Poll
    context_object_name = 'polls'
    ordering = ['-created_at']
