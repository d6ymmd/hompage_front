from django.shortcuts import render


def home(request):
    return render(request, 'base.html')

def notice_list(request):
    return render(request, 'home/notice_list.html')

def portfolio_list(request):
    return render(request, 'home/portfolio_list.html')

def portfolio_list2(request):
    return render(request, 'home/portfolio_list2.html')

def portfolio_list3(request):
    return render(request, 'home/portfolio_list3.html')