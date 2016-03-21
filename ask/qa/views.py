from django.shortcuts import render, render_to_response, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from qa.models import Question
from qa.forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def new_questions(request):
    limit = 10
    page = request.GET.get('page')
    paginator = Paginator(Question.objects.all().order_by('-pk'), limit)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render_to_response(
        'qa/questions_list.html', {'questions': questions})


def popular_questions(request):
    limit = 10
    page = request.GET.get('page')
    paginator = Paginator(Question.objects.all().order_by('-rating'), limit)
    try:
        questions = paginator.page(page)
    except PageNotAnInteger:
        questions = paginator.page(1)
    except EmptyPage:
        questions = paginator.page(paginator.num_pages)
    return render_to_response(
        'qa/questions_list.html', {'questions': questions})


def question_detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    form = AnswerForm(initial={'question': question_id})
    return render(request, 'qa/question_detail.html',
                  {'question': question, 'form': form})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST, user=request.user)
        if form.is_valid():
            question = form.save()
            return redirect('question_detail', question_id=question.id)
    else:
        form = AskForm(user=request.user)
    return render(request, 'qa/ask.html', {'form': form})


def answer(request):
    if request.method == 'POST':
        form = AnswerForm(request.POST, user=request.user)
        if form.is_valid():
            answer = form.save()
            return redirect('question_detail', question_id=answer.question_id)
    #else:
    #    form = AskForm(user=request.user)
    #return render(request, 'qa/ask.html', {'form': form})
