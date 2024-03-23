from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse("The is a new view!")


dynamic_pages = {
    'a': 'This is a dynamic view "A"',
    'b': 'This is a dynamic view "B"',
}


def dynamic_view(request, topic):
    try:
        return HttpResponse(dynamic_pages[topic])
    except KeyError:
        # return HttpResponseNotFound(f'"{topic}" page not found')
        raise Http404(f'"{topic}" page not found')


def sum(request, num_1, num_2):
    return HttpResponse(str(num_1 + num_2))
