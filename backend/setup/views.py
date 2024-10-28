from django.contrib.auth import authenticate, login
from django.http import HttpResponse

def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return HttpResponse("You're logged in.")
    else:
        return HttpResponse("Invalid login.")
