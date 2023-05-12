class RefreshBackMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.method == 'GET':
            if request.META.get('HTTP_REFERER') == request.build_absolute_uri() or 'refresh' in request.GET:
                # Clear session
                request.session.flush()
        
        response = self.get_response(request)
        
        return response
