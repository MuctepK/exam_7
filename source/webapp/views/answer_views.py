from django.shortcuts import render, redirect
from django.views.generic import CreateView
from django.views import View
from webapp.models import Poll, Answer, Choice


class CreateAnswerView(View):
    def get(self, request, *args, **kwargs):
        print(kwargs)
        poll = Poll.objects.get(pk = kwargs.get('pk'))
        choices = poll.choices.all()
        context = {'poll': poll,
                   'choices': choices}
        return render(request, 'answer/answer_create.html', context=context)

    def post(self, request, *args, **kwargs):
        poll = Poll.objects.get(pk = kwargs.get('pk'))
        print(request.POST)
        choice_pk = int(request.POST['choice_pk'])
        choice = Choice.objects.get(pk=choice_pk)
        Answer.objects.create(
            poll = poll,
            choice = choice
        )
        return redirect('create_answer', pk=poll.pk)