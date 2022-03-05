from django.http.response import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q

from .models import MarkerPack
from .forms import MarkersForm

# Create your views here.
def search(request):
    query = request.GET.get('q')
    mapid = request.GET.get('map')
    data = MarkerPack.objects.select_related("category", "added_by").all()
    if query and len(query) > 1:
        data = data.filter( Q(data__name__icontains=query) | Q(data__description__icontains=query))
            
    if mapid:
        print("Mapid: %s" % mapid)
        data = data.filter(data__markers__has_key=mapid)
    data = [x.query_result() for x in data[:10]]
    return JsonResponse({"result":data})

def get_markers(request, id):
    mp = get_object_or_404(MarkerPack, id=id)
    if mp:
        return JsonResponse(mp.data)

def download_markers(request, id):
    mp = get_object_or_404(MarkerPack, id=id)
    if mp:
        response = JsonResponse(mp.data, content_type='application/octet-stream')
        # TODO: Make mp.title filename safe
        response['Content-Disposition'] = 'attachment; filename=%s.etmp' % mp.title
        return response

def marker(request, id):
    mp = get_object_or_404(MarkerPack, id=id)
    return render(request, 'markers/marker.html', {"marker": mp})

def index(request):
    packs = MarkerPack.objects.order_by("-id")
    return render(request, 'markers/index.html', {"markers": packs})

@login_required
def submit_markers(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = MarkersForm(request.POST, request.FILES)
        # check whether it's valid:
        if form.is_valid():
            data = form.get_json()
            id = data['id']
            print(id)
            name = data['name']
            description = data.get('description') or ""
            category = form.cleaned_data["category"]

            try:
                entry = MarkerPack.objects.get(pack_id=id)
                print(entry)
                if entry.added_by == request.user:
                    # Update existing
                    entry.data = data
                    entry.updated = timezone.now()
                    entry.title = name
                    entry.category = category
                    entry.description = description
                    entry.save()
                else:
                    pass
                    # return error

            except ObjectDoesNotExist:
                entry = MarkerPack.objects.create(
                    data=data, 
                    title=name, 
                    pack_id=id,
                    added_by=request.user,
                    category=category,
                    description=description)
            return HttpResponseRedirect('/markers/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = MarkersForm()

    return render(request, 'markers/upload_markerpack.html', {'form': form})