from django.shortcuts import render

# Create your views here.


# Error Pages
def server_error(request):
    return render(request, 'errors/500.html')


def not_found(request):
    return render(request, 'errors/404.html')


def permission_denied(request):
    return render(request, 'errors/403.html')


def bad_request(request):
    return render(request, 'errors/400.html')