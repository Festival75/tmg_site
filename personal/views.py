from django.shortcuts import render


def index(request: 'request') -> None:
    """My index view"""
    return render(request, 'personal/home.html')
