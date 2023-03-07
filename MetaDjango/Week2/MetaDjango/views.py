from django.http import HttpResponse, HttpResponseNotFound


# Custom 404 error created 
def handler404(request,exception):
    return HttpResponse(" <h1 align=\"center\">404:Page Not Found!</h1>")

def home(request):
    return HttpResponseNotFound(" render with Http Response Not Found")  