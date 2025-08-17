# """
# URL configuration for mysite project.

# The `urlpatterns` list routes URLs to views. For more information please see:
#     https://docs.djangoproject.com/en/5.2/topics/http/urls/
# Examples:
# Function views
#     1. Add an import:  from my_app import views
#     2. Add a URL to urlpatterns:  path('', views.home, name='home')
# Class-based views
#     1. Add an import:  from other_app.views import Home
#     2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
# Including another URLconf
#     1. Import the include() function: from django.urls import include, path
#     2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
# """
# from django.contrib import admin
# from django.urls import path

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),

    # app urls
    # path('accounts/', include('accounts.urls')),   # register/login/logout
    # path('jobs/', include('jobs.urls')),           # job posting
    # path('resumes/', include('resumes.urls')),     # resume upload
    # path('applications/', include('applications.urls')),  # apply to jobs
    path('accounts/', include('accounts.urls')),
    path('applicants/', include('applicants.urls')),  # applicant dashboard at /applicants/dashboard/
    path('company/', include('company.urls')),      # company dashboard at /company/dashboard/
]


# Serve media & static files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)