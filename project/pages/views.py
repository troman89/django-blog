from django.shortcuts import render, redirect


def home(request):
    context = {}
    return render(request, 'pages/home.html', context)