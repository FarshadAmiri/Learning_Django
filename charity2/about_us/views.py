from django.shortcuts import render
from accounts.models import  User

def about_us(request):
    if request.method=='GET':
        users = User.objects.values_list('first_name', 'last_name')
        return render(request, 'about_us.html', context={'users':users})

