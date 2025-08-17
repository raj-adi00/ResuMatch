from django.shortcuts import redirect

class RoleBasedRedirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.exempt_urls = [
            '/accounts/login/',
            '/accounts/register/',
            '/admin/',
            '/accounts/',
        ]
        self.role_urls = {
            'applicant': '/applicants/dashboard/',
            'company': '/company/dashboard/',
        }

    def __call__(self, request):
        path = request.path

        # 1️⃣ Skip exempt URLs
        if any(path.startswith(url) for url in self.exempt_urls):
            return self.get_response(request)

        # 2️⃣ If user not authenticated → login
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')

        # 3️⃣ Root redirect to dashboard
        if path == '/':
            dashboard_url = self.role_urls.get(request.user.role)
            if dashboard_url:
                return redirect(dashboard_url)
            return redirect('/accounts/login/')  # fallback

        # 4️⃣ Role enforcement
        if path.startswith('/applicants/dashboard/') and request.user.role != 'applicant':
            return redirect(self.role_urls.get(request.user.role, '/accounts/login/'))
        if path.startswith('/company/dashboard/') and request.user.role != 'company':
            return redirect(self.role_urls.get(request.user.role, '/accounts/login/'))

        # 5️⃣ Proceed normally
        return self.get_response(request)
