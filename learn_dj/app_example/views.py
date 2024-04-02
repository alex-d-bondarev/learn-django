from pathlib import Path

from django.http import (
    Http404,
    HttpResponse,
    HttpResponseNotFound,
    HttpResponseRedirect,
)
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import TransactionForm
from .models import Transaction


# Create your views here.
def index(request):
    return HttpResponse('The is a new view!')


dynamic_pages = {
    'a': 'This is a dynamic view "A"',
    'b': 'This is a dynamic view "B"',
    'c': 'This is a dynamic view "C"',
}


def dynamic_view(request, topic):
    try:
        return HttpResponse(dynamic_pages[topic])
    except KeyError:
        # return HttpResponseNotFound(f'"{topic}" page not found')
        raise Http404(f'"{topic}" page not found')


def dynamic_mapping_view(request, num_page):
    topics = list(dynamic_pages.keys())
    topic = topics[num_page]
    # return HttpResponseRedirect(f'/app_example/{topic}/')

    webpage = reverse('topic-page', args=[topic])
    return HttpResponseRedirect(webpage)


def sum(request, num_1, num_2):
    return HttpResponse(str(num_1 + num_2))


def template_example(request):
    # app_example/templates/app_example/template_example.html

    template_vars = {
        'first_name': 'Rosalind',
        'last_name': 'Franklin',
        'some_list': [1, 2, 3],
        'some_dict': {
            'inside_key': 'inside_value',
            'key_2': 'value_2',
        },
        'user_logged_in': False,
    }

    return render(
        request, 'app_example/template_example.html', context=template_vars
    )


def links(request):
    return render(request, 'app_example/links.html')


def all_transactions(request):
    all_transactions = {'transactions': Transaction().get_all()}
    return render(
        request, 'app_example/transactions.html', context=all_transactions
    )


def new_transaction(request):

    if request.method == 'POST':
        form = TransactionForm(request.POST)
        if form.is_valid():
            Transaction().insert_new(form.cleaned_data)
            return redirect(reverse('app_example:transactions'))
    else:
        form = TransactionForm()
        context = {'form': form}
        return render(
            request, 'app_example/new_transaction.html', context=context
        )


def hello(request):
    hello_path = Path(__file__).resolve().parent / 'files' / 'hello.html'
    with open(hello_path) as h_file:
        return HttpResponse(h_file.read())
