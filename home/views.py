from django.shortcuts import render
from event.models import event
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

def index(request):
    events =  event.objects.all().filter(is_open=True)
    paginator = Paginator(events, 6)
    page = request.GET.get('page')
    page_events = paginator.get_page(page)


    context = {
        'events':page_events

    }
    return render(request,'home/index.html',context)
def search(request):
    query_set = event.objects.all()
    if 'city' in request.GET:
        keyword =  request.GET['city']
        if keyword:
            query_set =  query_set.filter(city__iexact=keyword)
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            query_set =  query_set.filter(title__icontains=keyword)
    if 'location' in request.GET:
        location = request.GET['location']
        if location:
            query_set = query_set.filter(place__icontains= location)

    context = {
        'events':query_set,
        'values': request.GET
    }
    return render(request,'home/search.html',context)