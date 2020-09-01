"""Middleware"""

from oso import OsoException

from .auth import request_authorized

def RequireAuthorization(get_response):
    """Check that ``authorize`` was called during the request."""
    def middleware(request):
        response = get_response(request)

        # Ensure authorization occurred.
        if not request_authorized(request):
            raise OsoException("authorize was not called during processing request.")

        return response

    return middleware
