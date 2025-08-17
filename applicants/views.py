from django.shortcuts import render
from accounts.middleware import RoleBasedRedirectMiddleware

def dashboard_view(request):
    return render(request, 'applicants/dashboard.html')