from django.contrib.auth.models import AnonymousUser

from .models import User

class DummyAuthBackend:
    """ """

def get_user(get_response):
    def middleware(request):
        email = request.headers.get('user')
        if email:
            request.user = User.objects.filter(email=email).first()
            if request.user is None:
                raise ValueError("User not found")
        else:
            request.user = AnonymousUser()

        return get_response(request)

    return middleware
