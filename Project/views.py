from django.shortcuts import render


def home(request):
    return render(request, 'index.html')  # Ensure 'index.html' exists

def frontend_view(request):
    return render(request, 'index.html')

def learning_page(request):
    return render(request, 'learning_page.html')  # Create this HTML file

def contact(request):
    return render(request, 'contact.html')

def network(request):
    return render(request, 'network.html')
