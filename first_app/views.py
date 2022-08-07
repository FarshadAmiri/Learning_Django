from django.shortcuts import render, HttpResponse

def signup_view(request):
    name = request.GET.get('name')
    username = request.GET.get('username')
    # return HttpResponse(f'You Successfully Signed up Dear {name}!\n Your username: {username}')
    return HttpResponse('You Successfully Signed up')
# Create your views here.
