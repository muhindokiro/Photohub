from django.shortcuts import render
from django.http  import HttpResponse
from .models import Photo

# Create your views here
def home(request):    
    return render(request, 'home.html')

def search_results(request):

    if 'photo' in request.GET and request.GET["photo"]:
        search_term = request.GET.get("photo")
        searched_photos = Photo.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"photos": searched_photos})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

def photo(request,photo_id):
    try:
        photo = Photo.objects.get(id = photo_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"home.html", {"photo":photo})




