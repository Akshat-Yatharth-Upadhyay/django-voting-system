from django.contrib import messages
from django.http import Http404
from django.shortcuts import get_object_or_404, redirect, render
from django.utils import timezone
from .models import Question, Choice


def index(request):
    questions = Question.objects.order_by('-pub_date')[:10]
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method != 'POST':
        return redirect('polls:detail', question_id=question.id)
    choice_id = request.POST.get('choice')
    if not choice_id:
        messages.error(request, 'Please select an option before voting.')
        return redirect('polls:detail', question_id=question.id)
    try:
        selected_choice = question.choices.get(pk=choice_id)
    except Choice.DoesNotExist:
        raise Http404('Selected choice does not exist.')
    selected_choice.votes += 1
    selected_choice.save(update_fields=['votes'])
    messages.success(request, 'Your vote has been recorded successfully!')
    return redirect('polls:results', question_id=question.id)


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    total_votes = sum(choice.votes for choice in question.choices.all())
    choices = []
    for choice in question.choices.all():
        percentage = round((choice.votes / total_votes) * 100, 1) if total_votes else 0
        choices.append({'choice': choice, 'percentage': percentage})
    return render(request, 'polls/results.html', {
        'question': question,
        'choices': choices,
        'total_votes': total_votes,
    })
