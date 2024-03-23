from django.http import HttpResponse, HttpResponseNotFound, Http404, HttpResponseRedirect


# Create your views here.
def index(request):
    return HttpResponse("The is a new view!")


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
    return HttpResponseRedirect(f'/app_example/{topic}/')


def sum(request, num_1, num_2):
    return HttpResponse(str(num_1 + num_2))
