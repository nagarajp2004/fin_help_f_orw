from django.shortcuts import render



def frontend_view(request):
    return render(request, 'index.html')

