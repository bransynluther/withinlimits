import search

# Create your views here.

def searchAPI(request):
    results = search.RestSearch(request.params["lat"], request.params["lng"], request.params["budget"])
    return results["results"]

