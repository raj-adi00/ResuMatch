from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'company/dashboard.html')
