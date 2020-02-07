from django.shortcuts import render


def home(request):
    return render(request, 'base.html')

def notice_list(request):
    return render(request, 'home/notice_list.html')

def portfolio_list(request):
    return render(request, 'home/portfolio_list.html')
